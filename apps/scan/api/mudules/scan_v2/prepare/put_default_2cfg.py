# coding:utf-8
import os
import re
from configparser import ConfigParser

from website.settings import PROJECT_DIR
SCAN_CONFIG_FILE = os.path.join(PROJECT_DIR, "apps", "scan", "config.ini")

from .....models import Protocol, NmapServiceName, ScanTool, Scheme

def orm_delete():
    Scheme.objects.all().delete()
    ScanTool.objects.all().delete()
    NmapServiceName.objects.all().delete()
    Protocol.objects.all().delete()


def inintal_services(config_file=SCAN_CONFIG_FILE, add_many=True):
    Protocol.objects.all().delete()
    NmapServiceName.objects.all().delete()

    config = ConfigParser(allow_no_value=True)
    config.read([config_file])

    supported_services = []
    for (protocol, val) in config.items("nmap-service-names"):
        services = val.split(",")
        _protocol, _slug = Protocol.objects.get_or_create(protocol=protocol)
        # supported_protocols.append(_protocol)
        for servicename in services:
            service = NmapServiceName(protocol=_protocol, service_name=servicename)
            supported_services.append(service)
            if not add_many:
                try:
                    service.save()
                except:
                    _info = "操作[" + servicename + "]到数据库失败！"
                    try:
                        from services.models import PlatOptHistory
                        PlatOptHistory.objects.create(desc=_info)
                    except:
                        import logging
                        logging.error(_info)
    if add_many:
        try:
            NmapServiceName.objects.bulk_create(supported_services)
        except:
            # 多条同时插入插入失败的情况下就用这个。
            inintal_services(add_many=False)


def inital_scan_tools():
    ScanTool.objects.all().delete()

    config = ConfigParser(allow_no_value=True)
    config.read([SCAN_CONFIG_FILE])
    
    scan_tools = []
    supported_protocols = Protocol.objects.all()
    for protocol in supported_protocols:
        for (name, used_script) in config.items(protocol.protocol):

            args = ",".join(re.findall("\[(.*?)\]", used_script))
            _scan_tool = ScanTool(name=name, used_script=used_script, args=args, protocol=protocol)
            scan_tools.append(_scan_tool)
    ScanTool.objects.bulk_create(scan_tools)


def inital_scheme():
    """
    当前实验只有Nmap脚本的示例
    :return:
    """
    Scheme.objects.all().delete()

    scheme_nmap = Scheme(name="scheme_nmap", desc="Nmap方案")
    scheme_all = Scheme(name="scheme_all", desc="所有扫描配置的方案")

    scheme_nmap.save()
    scheme_all.save()

    for x in ScanTool.objects.all():
        have_installed_tools = ["nmap", ]
        _tool_sets = "|".join(have_installed_tools)
        matched = re.match("^({}).*?".format(_tool_sets), x.used_script)
        scheme_all.scan_tools.add(x)
        if matched:
            scheme_nmap.scan_tools.add(x)


def inital_scan_cfgs(config_file=SCAN_CONFIG_FILE):
    #orm_delete()

    inintal_services(config_file=config_file)
    inital_scan_tools()
    inital_scheme()

    import logging
    logging.warning("初始化完成")

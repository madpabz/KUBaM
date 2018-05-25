import unittest
from ucsc import UCSCSession, UCSCServer, UCSCEquipment


class UCSCUnitTests(unittest.TestCase):
    """
    Tests for connecting to UCS Central
    """
    session = UCSCSession()
    handle, err = session.login("admin", "cisco.123", "10.94.132.71")

    def test_serverlist(self):
        servers = UCSCEquipment.list_servers(self.handle)
        #print servers
        assert(servers != "")

    def test_templatelist(self):
        templates = UCSCServer.list_templates(self.handle)
        #print templates
        assert(templates != "")

    def test_sp_crud(self):
        err, msg = UCSCServer.create_server(self.handle, "org-root/ls-TestTemplate", "test_kubam_sp", "org-root")
        #print err, msg
        assert(err == 0)
        
        err, msg = UCSCServer.delete_server(self.handle, "test_kubam_sp", "org-root")
        #print err, msg
        assert(err == 0)
import uno
import string
import unohelper
import xmlrpclib
from com.sun.star.task import XJobExecutor
if __name__<>"package":
    from lib.gui import *
    from lib.error import ErrorDialog
    from lib.functions import *
    from lib.logreport import *
    from Change import *
    database="test"

class ServerParameter( unohelper.Base, XJobExecutor ):
    def __init__(self,ctx):
        self.ctx     = ctx
        self.module  = "openerp_report"
        self.version = "0.1"
        desktop=getDesktop()
        log_detail(self)
        self.logobj=Logger()
        doc = desktop.getCurrentComponent()
        docinfo=doc.getDocumentInfo()
        self.win=DBModalDialog(60, 50, 160, 108, "Server Connection Parameter")

        self.win.addFixedText("lblVariable", 2, 12, 35, 15, "Server URL")
        if docinfo.getUserFieldValue(0)=="":
            docinfo.setUserFieldValue(0,"http://localhost:8069")
        self.win.addEdit("txtHost",-34,9,91,15,docinfo.getUserFieldValue(0))
        self.win.addButton('btnChange',-2 ,9,30,15,'Change', actionListenerProc = self.btnChange_clicked )

        self.win.addFixedText("lblDatabaseName", 6, 31, 31, 15, "Database")
        #self.win.addFixedText("lblMsg", -2,28,123,15)
        self.win.addComboListBox("lstDatabase", -2,28,123,15, True)
        self.lstDatabase = self.win.getControl( "lstDatabase" )
        #self.win.selectListBoxItem( "lstDatabase", docinfo.getUserFieldValue(2), True )
        #self.win.setEnabled("lblMsg",False)

        self.win.addFixedText("lblLoginName", 17, 51, 20, 15, "Login")
        self.win.addEdit("txtLoginName",-2,48,123,15,docinfo.getUserFieldValue(1))

        self.win.addFixedText("lblPassword", 6, 70, 31, 15, "Password")
        self.win.addEdit("txtPassword",-2,67,123,15,)
        self.win.setEchoChar("txtPassword",42)


        self.win.addButton('btnOK',-2 ,-5, 60,15,'Connect' ,actionListenerProc = self.btnOk_clicked )

        self.win.addButton('btnCancel',-2 - 60 - 5 ,-5, 35,15,'Cancel' ,actionListenerProc = self.btnCancel_clicked )
        sValue=""
        if docinfo.getUserFieldValue(0)<>"":
            res=getConnectionStatus(docinfo.getUserFieldValue(0))
            if res == -1:
                sValue="Could not connect to the server!"
                self.lstDatabase.addItem("Could not connect to the server!",0)
            elif res == 0:
                sValue="No Database found !!!"
                self.lstDatabase.addItem("No Database found !!!",0)
            else:
                self.win.removeListBoxItems("lstDatabase", 0, self.win.getListBoxItemCount("lstDatabase"))
		for i in range(len(res)):
                    self.lstDatabase.addItem(res[i],i)
                sValue = database

        self.win.doModalDialog("lstDatabase",sValue)

        #self.win.doModalDialog("lstDatabase",docinfo.getUserFieldValue(2))

    def btnOk_clicked(self,oActionEvent):
        sock = xmlrpclib.ServerProxy(self.win.getEditText("txtHost")+'/xmlrpc/common')
        sDatabase=self.win.getListBoxSelectedItem("lstDatabase")
        sLogin=self.win.getEditText("txtLoginName")
        sPassword=self.win.getEditText("txtPassword")
        UID = sock.login(sDatabase,sLogin,sPassword)
        if not UID :
            ErrorDialog("Connection Refuse...","Please enter valid Login/Password")
            self.win.endExecute()
        try:
            sock_g = xmlrpclib.ServerProxy(self.win.getEditText("txtHost") +'/xmlrpc/object')
            ids  = sock_g.execute(sDatabase,UID,sPassword, 'res.groups' ,  'search', [('name','=','OpenOfficeReportDesigner')])
            ids_module = sock_g.execute(sDatabase, UID, sPassword, 'ir.module.module', 'search', [('name','=','base_report_designer'),('state', '=', 'installed')])
            dict_groups = sock_g.execute(sDatabase, UID,sPassword, 'res.groups' , 'read',ids,['users'])
        except :
            import traceback,sys
            info = reduce(lambda x, y: x+y, traceback.format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback))
            self.logobj.log_write('ServerParameter', LOG_ERROR, info)

        if not len(ids) :
            ErrorDialog("Group Not Found!!!  Create a group  named  \n\n"'"OpenOfficeReportDesigner"'"  \n\n  ","","Group Name Error")
            self.logobj.log_write('Group Error',LOG_WARNING, ':Create a  group OpenOfficeReportDesigner   using database %s' % (sDatabase))
            self.win.endExecute()
        if not len(ids_module):
            ErrorDialog("Please Install base_report_designer module", "", "Module Uninstalled Error")
            self.logobj.log_write('Module Not Found',LOG_WARNING, ':base_report_designer not install in  database %s' % (sDatabase))
            self.win.endExecute()

        if UID not in dict_groups[0]['users']:
            ErrorDialog("Connection Refuse...","You have not access these Report Designer")
            self.logobj.log_write('Connection Refuse',LOG_WARNING, " Not Access Report Designer ")
            self.win.endExecute()
        else:
            desktop=getDesktop()
            doc = desktop.getCurrentComponent()
            docinfo=doc.getDocumentInfo()
            docinfo.setUserFieldValue(0,self.win.getEditText("txtHost"))
            docinfo.setUserFieldValue(1,self.win.getEditText("txtLoginName"))
            global passwd
            passwd=self.win.getEditText("txtPassword")
            global loginstatus
            loginstatus=True
            global database
            database=sDatabase
            global uid
            uid=UID
            #docinfo.setUserFieldValue(2,self.win.getListBoxSelectedItem("lstDatabase"))
            #docinfo.setUserFieldValue(3,"")

            ErrorDialog(" You can start creating your report in \n  \t the current document.","After Creating  sending to the server.","Message")
            self.logobj.log_write('successful login',LOG_INFO, ':successful login from %s  using database %s' % (sLogin, sDatabase))
            self.win.endExecute()

    def btnCancel_clicked( self, oActionEvent ):
        self.win.endExecute()

    def btnChange_clicked(self,oActionEvent):
        aVal=[]
        url= self.win.getEditText("txtHost")
        Change(aVal,url)
        if aVal[1]== -1:
            ErrorDialog(aVal[0],"")
        elif aVal[1]==0:
            ErrorDialog(aVal[0],"")
        else:
            self.win.setEditText("txtHost",aVal[0])
            self.win.removeListBoxItems("lstDatabase", 0, self.win.getListBoxItemCount("lstDatabase"))
            for i in range(len(aVal[1])):
                self.lstDatabase.addItem(aVal[1][i],i)


if __name__<>"package" and __name__=="__main__":
    ServerParameter(None)
elif __name__=="package":
    g_ImplementationHelper.addImplementation( ServerParameter, "org.openoffice.openerp.report.serverparam", ("com.sun.star.task.Job",),)


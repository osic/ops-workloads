import yaml
import sys
import importlib
class parser_task():
    def __init__(self,name):
          self.file_name=name
    def parse(self):
          file=open(self.file_name)
          stream=yaml.load(file)
          for key,value in stream.iteritems():
              plugin_name=key.split('.')[0]
              pkg=sys.path.append("/opt/ops-workload-framework/heat_workload/plugins/"+plugin_name)
              class_name=key.split('.')[1]
              print "Task: "+class_name+" started..."
              new_module = importlib.import_module(class_name,pkg)
              mod=getattr(new_module,class_name)
              obj=mod(**value)
              obj.run()

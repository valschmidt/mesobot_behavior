import py_trees
from mesobot_blackboard import bhv_bb

class RepositionMesobotAction(py_trees.behaviour.Behaviour):
    '''Behavior to determine if Mesobot Location is known.'''
    def __init__(self,name):
        super(RepositionMesobotAction,self).__init__(name)

    def setup(self,timeout):
        return True
    def initialise(self):
        pass

    def update(self):
        '''Reposition Mesobot.'''

        self.logger.debug("  %s [RepositionMesobotAction::update()]" % self.name)
        return py_trees.common.Status.SUCCESS
    
    def terminate(self,new_status):
        pass
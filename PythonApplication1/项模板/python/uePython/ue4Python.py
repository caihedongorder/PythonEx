
import os
import sys

import unreal_engine as ue
from unreal_engine import FVector, FRotator

from utils.ue4.uobject_util import ObjectUtil
from utils.ue4.actor_util import ActorUtil
from utils.ue4.component_util import ComponentUtil
from utils.ue4.material_util import MaterialUtils


#import rpdb2;
#rpdb2.start_embedded_debugger("test",timeout=0)

#from utils.ue4 import debugger
#debugger.start_winpdb()


class $safeitemname$:

    # this is called on game start
    def begin_play(self):
        print('Begin Play')
    def end_play(self,reason):
        print('End Play')
        
    # this is called at every 'tick'    
    def tick(self, delta_time):
        # get current location
        pass

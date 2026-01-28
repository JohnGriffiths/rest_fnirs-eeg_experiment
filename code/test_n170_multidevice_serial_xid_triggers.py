
"""
Run experiment script
"""

"""
#from eegnb.experiments.rest.eoec import RestEyesOpenCloseAlternating
from eegnb.experiments.visual_n170.n170 import VisualN170
from eegnb.devices.eeg import EEG  as eegexpy_device

dev_xid = eegexpy_device(device="nirsport2", xid_num = 1) #, xid_num=1)  
#dev_xid.push_sample(marker=2, timestamp=0) # note that timestamp is not currently used
                                                                           # in this context
# for the nirx nirsport2 the above can be viewed and checked at the bottom of the aurora 
# recording software

dev_ser = eegexpy_device(device="biosemi", serial_port="COM4")
#dev_ser.push_sample(marker=2, timestamp=0) # note that timestamp is not currently used


thisexp = VisualN170(eeg = dev_xid, duration=15)#devices=[dev_xid, dev_ser], duration=15)
thisexp.use_fullscr = False # best for debugging
thisexp.screen_num = 1
thisexp.run()


#thisexp = VisualN170(devices=[dev_ser, dev_xid], 
#                     duration=15, use_fullscr=False, screen_num=1)  


thisexp.run()
"""


# Run eeg-expy visual n170 with biosemi serial triggers
from eegnb.experiments.visual_n170.n170 import VisualN170
from eegnb.devices.eeg import EEG

thisxid = EEG(device="nirsport2", xid_num = 1) #, xid_num=1)  
thiseeg = EEG(device="biosemi", serial_port="COM4")
#thisexp = VisualN170(eeg=thiseeg, duration=15)
thisexp = VisualN170(devices=[thiseeg, thisxid], duration=20)# 600)
thisexp.use_fullscr = False # best for debugging
thisexp.screen_num = 1
thisexp.run()



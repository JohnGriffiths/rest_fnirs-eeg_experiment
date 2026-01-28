
"""
Run eeg-expy eoec with biosemi serial triggers and nirx xid2 triggers
"""

from eegnb.experiments.rest.eoec import RestEyesOpenCloseAlternating
from eegnb.devices.eeg import EEG

thisxid = EEG(device="nirsport2", xid_num = 1) 
thiseeg = EEG(device="biosemi", serial_port="COM4")
thisexp = RestEyesOpenCloseAlternating(devices=[thiseeg, thisxid], duration=600)
thisexp.use_fullscr = False # best for debugging
thisexp.screen_num = 1
thisexp.run()



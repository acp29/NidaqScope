# Example python dictionaries for telegraphs
#gains = {0.5:0.05, 1.0:0.1, 1.5:0.2, 2.0:0.5, 2.5:1.0, 3.0:2.0, 3.5:5.0, 4.0:10.0, 4.5:20.0, 5.0:50.0, 5.5:100.0, 6.0:200.0, 6.5:500.0}
#fcs = {2.0:1000, 4.0:2000, 6.0:5000, 8.0:10000, 10.0:50000}
#modes = {1.0:'V', 2.0:'V', 4.0:'V', 6.0:'A'}

#pip install nptdms
#pip install pyqtgraph
#pip install nidaqmx
#pip install numpy
#pip install hdf5storage

import sip
sip.setapi('QString',2)
sip.setapi('QVariant',2)

from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import nidaqmx
import time
import os
import sys
import datetime
import pyqtgraph as pg

import re
from nidaqmx.stream_readers import AnalogSingleChannelReader

def get_gain(ai_channel = "Dev1/ai7", config = "DIFFERENTIAL", gaintele = ''):
    try:
        gaintask = nidaqmx.Task()
        gaintask.ai_channels.add_ai_voltage_chan(ai_channel,
            terminal_config=eval("nidaqmx.constants.TerminalConfiguration.%s" % (config)),
            min_val=-10.0, max_val=10.0,
            units=nidaqmx.constants.VoltageUnits.VOLTS)
        reader = AnalogSingleChannelReader(gaintask.in_stream)
        gain_volts = reader.read_one_sample()
        gainteledict = eval('{' + gaintele + '}')
        gainlist = re.split(':|, |{|}',gaintele)
        del gainlist[1::2]
        gainlist = map(float, gainlist)
        gain_volts = min(gainlist, key=lambda x:abs(gain_volts-x))#0.1*np.round(10*gain_volts)
        #gains = {0.5:0.05, 1.0:0.1, 1.5:0.2, 2.0:0.5, 2.5:1.0, 3.0:2.0, 3.5:5.0, 4.0:10.0, 4.5:20.0, 5.0:50.0, 5.5:100.0, 6.0:200.0, 6.5:500.0}
        gain = gainteledict.get(gain_volts)
    except:
		gain = 'gainfail'
    finally:
        return gain
		

def get_fc(ai_channel = "Dev1/ai5", config = "DIFFERENTIAL", fctele = ''):
	try:
		fctask = nidaqmx.Task()
		fctask.ai_channels.add_ai_voltage_chan(ai_channel,
			terminal_config=eval("nidaqmx.constants.TerminalConfiguration.%s" % (config)),
			min_val=-10.0, max_val=10.0,
			units=nidaqmx.constants.VoltageUnits.VOLTS)
		reader = AnalogSingleChannelReader(fctask.in_stream)
		fc_volts = reader.read_one_sample()
		fcteledict = eval('{' + fctele + '}')
		fclist = re.split(':|, |{|}',fctele)
		del fclist[1::2]
		fclist = map(float, fclist)
		fc_volts = min(fclist, key=lambda x:abs(fc_volts-x))
		#fcs = {2.0:1000, 4.0:2000, 6.0:5000, 8.0:10000, 10.0:50000}
		fc = fcteledict.get(fc_volts)
	except: 
		fc = 'fcfail'
	finally:
		return fc

def get_mode(ai_channel = "Dev1/ai6", config = "DIFFERENTIAL", modetele = '' ):
    try:
		modetask = nidaqmx.Task()
		modetask.ai_channels.add_ai_voltage_chan(ai_channel,
			terminal_config=eval("nidaqmx.constants.TerminalConfiguration.%s" % (config)),
			min_val=-10.0, max_val=10.0,
			units=nidaqmx.constants.VoltageUnits.VOLTS)
		reader = AnalogSingleChannelReader(modetask.in_stream)
		modeteledict = eval('{' + modetele + '}')
		modelist = re.split(':|, |{|}',modetele)
		del modelist[1::2]
		modelist = map(float, modelist)
		mode_volts = reader.read_one_sample()
		mode_volts = min(modelist, key=lambda x:abs(mode_volts-x))
		#modes = {1.0:'V', 2.0:'V', 4.0:'V', 6.0:'A'}
		mode = modeteledict.get(mode_volts)
    except:
        mode = 'modefail'
    finally:
		return mode

def scope(save=False,
    rate=20000,
    win_size=1,
    ai_channel="Dev1/ai0", 
    save_dir=".",
    config="DIFFERENTIAL",
    limits=[-10.0,10.0],
    unit='V',
    scale=1,
    gain=1,
    notes="",
    prepulse=0,
    pulse_amp=0,
    pulse_length=0,
    postpulse=0,
    holding_voltage=0,
    commander_scale=0,
    pulse=False):
 
    # Command line tool for scroll-type free-running 2-channel oscilloscope for analogue inputs to National Instruments DAQ devices 
    # Example usage:
    #  import nidaq_scope
    #  nidaq_scope.scope(save=True,ai_channel=["Dev1/ai0","Dev1/ai2"])
    #  nidaq_scope.scope(save=True,ai_channel="Dev1/ai1",win_size=5,unit='A',gain=20)

    if unit!='A' and unit!='V':
      raise ValueError('The unit must be either V or A')

    # Set filename for data logging
    os.chdir(save_dir)
    if save == True:
        d = str(datetime.date.today()).replace("-","")
        ls = os.listdir(".")
        flist = []
        [flist.append(i) for i in ls if i[0:9]=="%s_" % (d) ]
        flist.sort()
        if not flist:
            fname = "%s_%03u" % (d,0)
        elif flist[-1][9:12] == '000':
            fname = "%s_%03u" % (d,1)
        else:
            fname = "%s_%03u" % (d,eval(flist[-1][9:12].lstrip("0"))+1)

    # Parameters
    N = int(win_size*rate)
    n = 100
    if isinstance(ai_channel,list):
        if ai_channel[0][0] == '/':
            ai_channel[0] = ai_channel[0].replace('/','',1)
        if len(ai_channel)>1:
            if ai_channel[1][0] == '/':
                ai_channel[1]=ai_channel[1].replace('/','',1)        
        ai_channel_list = ai_channel
        ai_channel = "%s,%s" % (ai_channel_list[0],ai_channel_list[1])  
    else:
        if ai_channel[0] == '/':
            ai_channel = ai_channel.replace('/','',1)
        ai_channel_list = [ai_channel] 
    nChannels = len(ai_channel_list)	
    if nChannels > 1:
        ao_channel_list = [i.replace('ai','ao') for i in ai_channel_list]
    else:
        ao_channel = ai_channel.replace('ai','ao')
	
    # Initialize
    task = nidaqmx.Task()
    if nChannels > 1:
        task.ai_channels.add_ai_voltage_chan(ai_channel_list[0],
            terminal_config=eval("nidaqmx.constants.TerminalConfiguration.%s" % (config)),
            min_val=min(limits), max_val=max(limits),
            units=nidaqmx.constants.VoltageUnits.VOLTS)
        task.ai_channels.add_ai_voltage_chan(ai_channel_list[1],
            terminal_config=eval("nidaqmx.constants.TerminalConfiguration.%s" % (config)),
            min_val=min(limits), max_val=max(limits),
            units=nidaqmx.constants.VoltageUnits.VOLTS)
    else: 
        task.ai_channels.add_ai_voltage_chan(ai_channel,
            terminal_config=eval("nidaqmx.constants.TerminalConfiguration.%s" % (config)),
            min_val=min(limits), max_val=max(limits),
            units=nidaqmx.constants.VoltageUnits.VOLTS)
    if pulse == True:
        pulsetask = nidaqmx.Task()
        if nChannels > 1:
            pulsetask.ao_channels.add_ao_voltage_chan(ao_channel_list[0], min_val = -10, max_val = 10);
            pulsetask.ao_channels.add_ao_voltage_chan(ao_channel_list[1], min_val = -10, max_val = 10);
        else:
            pulsetask.ao_channels.add_ao_voltage_chan(ao_channel, min_val = -10, max_val = 10);
        pulserate=100
        wavepre=[holding_voltage*(1000/commander_scale)]*int(prepulse*pulserate);
        wavestep=[(holding_voltage+pulse_amp)*(1000/commander_scale)]*int(pulse_length*pulserate)
        wavepost=[holding_voltage*(1000/commander_scale)]*int(postpulse*pulserate)
        wave = wavepre+wavestep+wavepost
        if nChannels > 1:
            wave = [wave,wave]
        pulsetask.timing.cfg_samp_clk_timing(rate = 100, sample_mode=nidaqmx.constants.AcquisitionType.CONTINUOUS, samps_per_chan=len(wave));
        pulsetask.write(data=wave, auto_start=False)
    if save == True:
        task.in_stream.configure_logging(fname,nidaqmx.constants.LoggingMode.LOG_AND_READ)
    task.timing.cfg_samp_clk_timing(rate, sample_mode=nidaqmx.constants.AcquisitionType.CONTINUOUS)
    task.in_stream.input_buf_size = n*100
    task.in_stream.auto_start=True
    non_local_var = {'x': np.zeros(N),
                     'y1': np.zeros(N),'y2': np.zeros(N),
                     'xscan': (1+np.arange(0,n,1.0,dtype='float64'))/rate,
                     'yscan1': [],'yscan2': [],
                     'nChannels':0, 'count': 0.0}
    xRef = np.arange(0,N,1.0,dtype='float64')/rate

    # Start continuous acquisition task
    def callback(task_handle, every_n_samples_event_type, number_of_samples, callback_data):
        Y = task.read(number_of_samples_per_channel=n)
        # scroll
        x = non_local_var['x']
        y1 = non_local_var['y1']
        y2 = non_local_var['y2']
        x[0:-1*n] = x[n:]
        x[-1*n:] = (1+np.arange(0,n,1.0,dtype='float64'))/rate + x[-1*n-1]
        if len(Y)==n:
            non_local_var['nChannels'] = 1
            y1[0:-1*n] = y1[n:]
            y1[-1*n:] = Y
            non_local_var['y1'] = y1
        elif len(Y)==2:
            non_local_var['nChannels'] = 2
            y1[0:-1*n] = y1[n:]
            y1[-1*n:] = Y[0]
            non_local_var['y1'] = y1
            y2[0:-1*n] = y2[n:]
            y2[-1*n:] = Y[1]
            non_local_var['y2'] = y2
        non_local_var['x'] = x
        # scan
        x = non_local_var['xscan']
        y1 = non_local_var['yscan1']
        y2 = non_local_var['yscan2'] 
        if len(Y)==n:
            non_local_var['nChannels'] = 1
            if (len(y1) == 0):
                x = (win_size*non_local_var['count'])+(1+np.arange(0,n,1.0,dtype='float64'))/rate
                y1 = np.array(Y)
            if (len(x) < (rate*win_size)):
                x = np.append(x,(1+np.arange(0,n,1.0,dtype='float64'))/rate + x[-1])
                y1 = np.append(y1,Y)
            else:
                non_local_var['count'] += 1.0
                x = (win_size*non_local_var['count'])+(1+np.arange(0,n,1.0,dtype='float64'))/rate
                y1 = np.array(Y)
                p2.setRange(xRange=[(i+(win_size*non_local_var['count'])) for i in [0,win_size]])
            non_local_var['yscan1'] = y1
        elif len(Y)==2:        
            non_local_var['nChannels'] = 2
            if (len(y1) == 0):
                x = (win_size*non_local_var['count'])+(1+np.arange(0,n,1.0,dtype='float64'))/rate
                y1 = np.array(Y[0])
                y2 = np.array(Y[1])
            if (len(x) < (rate*win_size)):
                x = np.append(x,(1+np.arange(0,n,1.0,dtype='float64'))/rate + x[-1])
                y1 = np.append(y1,Y[0])
                y2 = np.append(y2,Y[1])
            else:
                non_local_var['count'] += 1.0
                x = (win_size*non_local_var['count'])+(1+np.arange(0,n,1.0,dtype='float64'))/rate
                y1 = np.array(Y[0])
                y2 = np.array(Y[1])
                p2.setRange(xRange=[(i+(win_size*non_local_var['count'])) for i in [0,win_size]])
            non_local_var['yscan1'] = y1
            non_local_var['yscan2'] = y2
        non_local_var['xscan'] = x  
        return 0

	
	
	
    # Start data logging
    task.register_every_n_samples_acquired_into_buffer_event(n, callback)
    if pulse==True:
        pulsetask.start()
    task.start()


    ##############################################################################
    # Run scrolling oscilloscope
    win1 = pg.GraphicsWindow()
    win1.setWindowTitle('Scrolling oscilloscope')
    win1.setGeometry(8,30,800,400)
    p1 = win1.addPlot()
    p1.setRange(xRange=[xRef[0],xRef[-1]])
    p1.setRange(yRange=[i*scale/gain for i in limits])
    p1.setMouseEnabled(x=False, y=True)
    if unit == 'A':
      p1.setLabel('left', "Current (A)")
    elif unit == 'V':
      p1.setLabel('left', "Voltage (V)")
    p1.setLabel('bottom', "Time (s)")
    p1.showGrid(x=True,y=True,alpha=1.0)
    curve1_1 = p1.plot(xRef,non_local_var['y1']*scale/gain,pen='y')
    if non_local_var['nChannels'] == 2:
        curve1_2 = p1.plot(xRef,non_local_var['y2']*scale/gain,pen='c')

    def update_plot():
       curve1_1.setData(xRef,non_local_var['y1']*scale/gain)
       if non_local_var['nChannels'] == 2:
          curve1_2.setData(xRef,non_local_var['y2']*scale/gain)
       sys.stdout.flush()
       sys.stdout.write("Time elapsed: %.2f seconds\r" % (non_local_var['x'][-1]))

    ##############################################################################

    ##############################################################################
    # Run scanning oscilloscope
    win2 = pg.GraphicsWindow()
    win2.setWindowTitle('Scanning oscilloscope')
    win2.setGeometry(8,468,800,400)
    p2 = win2.addPlot()
    p2.setRange(xRange=[non_local_var['xscan'][0],non_local_var['xscan'][0]+win_size])
    p2.setRange(yRange=[i*scale/gain for i in limits])
    p2.setMouseEnabled(x=True, y=True)
    if unit == 'A':
      p2.setLabel('left', "Current (A)")
    elif unit == 'V':
      p2.setLabel('left', "Voltage (V)")
    p2.setLabel('bottom', "Time (s)")
    p2.showGrid(x=True,y=True,alpha=1.0)
    curve2_1 = p2.plot(non_local_var['xscan'],non_local_var['yscan1']*scale/gain,pen='y')
    if non_local_var['nChannels'] == 2:
        curve2_2 = p2.plot(non_local_var['xscan'],non_local_var['yscan2']*scale/gain,pen='c')

    def update_scan():
       if len(non_local_var['xscan']) == len(non_local_var['yscan1']):
           curve2_1.setData(non_local_var['xscan'],non_local_var['yscan1']*scale/gain)
       if non_local_var['nChannels'] == 2:
           if len(non_local_var['xscan']) == len(non_local_var['yscan2']):
                curve2_2.setData(non_local_var['xscan'],non_local_var['yscan2']*scale/gain)    
      
    ##############################################################################

    ##############################################################################
    # Run baseline monitor
    winBin = pg.GraphicsWindow()
    winBin.setWindowTitle('Baseline monitor: Median binned data (%ss binwidth)' % (win_size))
    winBin.setGeometry(824,30,400,400)
    pBin = winBin.addPlot()
    pBin.showGrid(x=True,y=True,alpha=1.0)
    pBin.setRange(yRange=[i*scale/gain for i in limits])
    pBin.setMouseEnabled(x=False, y=True)
    if unit == 'A':
      pBin.setLabel('left', "Current (A)")
    elif unit == 'V':
      pBin.setLabel('left', "Voltage (V)")
    pBin.setLabel('bottom', "Time (s)")
    binX = []
    binY1 = []
    if non_local_var['nChannels'] == 2:
        binY2 = []
    curveBin1 = pBin.plot(np.array(binX),np.array(binY1)*scale/gain,symbol='o',symbolBrush='y',symbolPen='y',pen='y')
    if non_local_var['nChannels'] == 2: 
        curveBin2 = pBin.plot(np.array(binX),np.array(binY2)*scale/gain,symbol='o',symbolBrush='c',symbolPen='c',pen='c')

    def update_bin():
       binX.append(non_local_var['x'][-1])
       binY1.append(np.median(non_local_var['y1']))
       curveBin1.setData(np.array(binX),np.array(binY1)*scale/gain)
       if non_local_var['nChannels'] == 2:
           binY2.append(np.median(non_local_var['y2']))
           curveBin2.setData(np.array(binX),np.array(binY2)*scale/gain)
       pBin.setRange(xRange=[0,binX[-1]])

    ##############################################################################
    
    ##############################################################################
    # Run Pulse monitor
    if pulse == True:
        winPulse = pg.GraphicsWindow()
        winPulse.setWindowTitle('Window for Access Resistance')
        winPulse.setGeometry(824,468,400,400)
        pPulse = winPulse.addPlot()
        pPulse.showGrid(x=True,y=True,alpha=1.0)
        pPulse.setRange(yRange=[0,5e+07])
        pPulse.setMouseEnabled(x=False, y=True)    
        pPulse.setLabel('left', "Resistance(ohms)")
        pPulse.setLabel('bottom', "Time (s)")
        pulseX = []
        pulseY1 = []
        #pulseY1 = []
        curvePulse1 = pPulse.plot(np.array(pulseX),np.array(pulseY1)*scale/gain,symbol='o',symbolBrush='y',symbolPen='y',pen='y')
        #if non_local_var['nChannels'] == 2: 
        #    curvePulse2 = pPulse.plot(np.array(pulseX),np.array(pulseY1)*scale/gain,symbol='o',symbolBrush='c',symbolPen='c',pen='c')
    


    def prepare_update_pulse():
	    pg.QtCore.QTimer.singleShot((prepulse*1000)+200, update_pulse)

    def update_pulse():
	# Currently only works for 1 channel and for a negative test pulse
        pulseinfo = []
        pulseX.append(non_local_var['x'][-1])
        pulseinfo = non_local_var['yscan1'].tolist()
        while len(pulseinfo) < (rate/10):
            pulseinfo = non_local_var['yscan1'].tolist()
        pulse_max = min(pulseinfo)		
        pulse_baseline = pulseinfo[0:int(prepulse*1000)-200]
        median = np.median(pulse_baseline)*scale/gain
        diff = (pulse_max*scale/gain)-median
        res=abs(pulse_amp/diff)

        pulseY1.append(res)
        curvePulse1.setData(np.array(pulseX),np.array(pulseY1))
        pPulse.setRange(xRange=[0,pulseX[-1]])
		
    
    ##############################################################################    

    # Prepare plot updating tasks
    timer_scroll = pg.QtCore.QTimer()
    timer_scroll.timeout.connect(update_plot)
    timer_scan = pg.QtCore.QTimer()
    timer_scan.timeout.connect(update_scan)
    timer_bin = pg.QtCore.QTimer()
    timer_bin.timeout.connect(update_bin)
    timer_pulse = pg.QtCore.QTimer()
    timer_pulse.timeout.connect(prepare_update_pulse)
    if pulse is True:
        prepare_update_pulse()
        period = (prepulse+pulse_length+postpulse)*1000
        timer_pulse.start(period)

    # Start plot updating tasks
    timer_scroll.start(20)
    timer_scan.start(20)
    timer_bin.start(win_size*1000)   
       
    # End oscilloscope and data logging
    raw_input('Running task. Press Enter to stop recording and see accumulated samples.\n')
    timer_scroll.stop()
    timer_scan.stop()
    timer_bin.stop()
    timer_pulse.stop()
    task.stop()
    if pulse is True:
        pulsetask.stop()
        pulsetask.close()
    add_notes = raw_input('Type more notes and/or press Enter to close graphs and return to the console.\n')
    notes = notes + "\n" + add_notes
	
	
    if save is True:
        # Write binned data to text file
        if non_local_var['nChannels'] == 1: 
            np.savetxt("./%s_baseline.txt" % (fname),np.transpose(np.matrix([binX,np.array(binY1)*scale/gain])))
        elif non_local_var['nChannels'] == 2: 
            np.savetxt("./%s_baseline.txt" % (fname),np.transpose(np.matrix([binX,np.array(binY1)*scale/gain,np.array(binY2)*scale/gain])))
        if pulse is True:
            np.savetxt("./%s_access.txt" % (fname),np.transpose(np.matrix([pulseX,pulseY1])))
	# Write scale factor for acquired raw data to file and any other user notes
        f = open("./%s_notes.txt" % (fname),'w+')
	f.write("Scale factor to generate data from tdms file: %s\n" % (scale/gain))
        f.write(notes)
        f.close()
	   
def mc700scope(save=False,
    rate=20000,
    Fc=4000,
    win_size=1,
    ai_channel="Dev1/ai0", 
    save_dir=".",
    config="DIFFERENTIAL",
    limits=[-10.0,10.0],
    unit='A',
    scale=2e-9,
    gain=20,
    notes="",
    prepulse=0,
    pulse_amp=0,
    pulse_length=0,
    postpulse=0,
    holding_voltage=0,
    commander_scale=0,
    pulse=False):
 
    # See scroll for usage. Example:
    #   nidaq_scope.mc700scope(False,20000,2000,win_size=5,ai_channel="Dev1/ai1",unit='A',gain=20)
    #   nidaq_scope.mc700scope(True,20000,2000,win_size=5,ai_channel="Dev1/ai1",unit='A',gain=20)

    # This wrapper function sets the primary gain in both channels of the amplifier before starting scroll
    # Only works in 32-bit python. Multiclamp commander must be loaded before executing this function

    # acq4 must be on the python path for this to run. If it is not, then you must set the path here
    #path_to_acq4=str(path_to_acq4)
    #sys.path.append(path_to_acq4)
    #sys.path.append("/Users/Public/ProgramData32/acq4")

    # Set primary gain settings in both channels of the Multiclamp700
    from MultiClamp import MultiClamp # This is code from acq4
    mc = MultiClamp.instance()
    chans = mc.listChannels()
    for ch in chans:
        mcchan = mc.getChannel(ch)
        time.sleep(0.1)
        if unit=='A':
            mcchan.setMode('VC')
        elif unit=='V':
            mcchan.setMode('I=0') # Currently only current clamp with I=0 for the time being
        mcchan.setParams({'PrimarySignalGain':gain})
        mcchan.setParams({'PrimarySignalLPF':Fc})

    # Start scope
    scope(save, rate, win_size, ai_channel, save_dir, config, limits, unit, scale, gain, notes, prepulse, pulse_amp, pulse_length, postpulse, holding_voltage, commander_scale, pulse)

#Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

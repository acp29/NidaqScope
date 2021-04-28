# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Edit_Pulse.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Pulse_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(220, 470)
        Dialog.setMaximumSize(QtCore.QSize(220, 470))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 221, 471))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_17 = QtGui.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(0, 120, 111, 31))
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_16 = QtGui.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(0, 20, 111, 31))
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.pulse_length_spinner = QtGui.QDoubleSpinBox(self.frame)
        self.pulse_length_spinner.setGeometry(QtCore.QRect(110, 120, 91, 31))
        self.pulse_length_spinner.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.pulse_length_spinner.setDecimals(3)
        self.pulse_length_spinner.setMaximum(1.0)
        self.pulse_length_spinner.setSingleStep(0.01)
        self.pulse_length_spinner.setProperty("value", 0.02)
        self.pulse_length_spinner.setObjectName(_fromUtf8("pulse_length_spinner"))
        self.amplitude_spinner = QtGui.QDoubleSpinBox(self.frame)
        self.amplitude_spinner.setGeometry(QtCore.QRect(110, 70, 91, 31))
        self.amplitude_spinner.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.amplitude_spinner.setDecimals(3)
        self.amplitude_spinner.setMinimum(-10.0)
        self.amplitude_spinner.setMaximum(10.0)
        self.amplitude_spinner.setSingleStep(0.001)
        self.amplitude_spinner.setProperty("value", -0.01)
        self.amplitude_spinner.setObjectName(_fromUtf8("amplitude_spinner"))
        self.down_spinner_1 = QtGui.QDoubleSpinBox(self.frame)
        self.down_spinner_1.setGeometry(QtCore.QRect(110, 20, 91, 31))
        self.down_spinner_1.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.down_spinner_1.setDecimals(3)
        self.down_spinner_1.setMaximum(1000.0)
        self.down_spinner_1.setSingleStep(0.01)
        self.down_spinner_1.setProperty("value", 1.0)
        self.down_spinner_1.setObjectName(_fromUtf8("down_spinner_1"))
        self.label_18 = QtGui.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(0, 70, 111, 31))
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.down_spinner_2 = QtGui.QDoubleSpinBox(self.frame)
        self.down_spinner_2.setGeometry(QtCore.QRect(110, 170, 91, 31))
        self.down_spinner_2.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.down_spinner_2.setDecimals(3)
        self.down_spinner_2.setMaximum(1000.0)
        self.down_spinner_2.setSingleStep(0.01)
        self.down_spinner_2.setProperty("value", 0.98)
        self.down_spinner_2.setObjectName(_fromUtf8("down_spinner_2"))
        self.label_21 = QtGui.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(0, 170, 111, 31))
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.commander_scale_spinner = QtGui.QSpinBox(self.frame)
        self.commander_scale_spinner.setGeometry(QtCore.QRect(110, 270, 91, 31))
        self.commander_scale_spinner.setMaximum(1000.0)
        self.commander_scale_spinner.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.commander_scale_spinner.setObjectName(_fromUtf8("commander_scale_spinner"))
        self.label_19 = QtGui.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(0, 270, 111, 31))
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.frame_7 = QtGui.QFrame(self.frame)
        self.frame_7.setGeometry(QtCore.QRect(20, 320, 185, 45))
        self.frame_7.setFrameShape(QtGui.QFrame.Panel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setLineWidth(3)
        self.frame_7.setMidLineWidth(1)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.get_commander_scale_button = QtGui.QPushButton(self.frame)
        self.get_commander_scale_button.setGeometry(QtCore.QRect(22, 322, 181, 41))
        self.get_commander_scale_button.setToolTip(_fromUtf8(""))
        self.get_commander_scale_button.setObjectName(_fromUtf8("get_commander_scale_button"))
        self.show_wave_button = QtGui.QPushButton(self.frame)
        self.show_wave_button.setGeometry(QtCore.QRect(22, 374, 181, 41))
        self.show_wave_button.setObjectName(_fromUtf8("show_wave_button"))
        self.frame_9 = QtGui.QFrame(self.frame)
        self.frame_9.setGeometry(QtCore.QRect(20, 372, 185, 45))
        self.frame_9.setFrameShape(QtGui.QFrame.Panel)
        self.frame_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_9.setLineWidth(3)
        self.frame_9.setMidLineWidth(1)
        self.frame_9.setObjectName(_fromUtf8("frame_9"))
        self.close_window = QtGui.QPushButton(self.frame)
        self.close_window.setGeometry(QtCore.QRect(80, 432, 71, 31))
        self.close_window.setObjectName(_fromUtf8("close_window"))
        self.holding_voltage_spinner = QtGui.QDoubleSpinBox(self.frame)
        self.holding_voltage_spinner.setGeometry(QtCore.QRect(110, 220, 91, 31))
        self.holding_voltage_spinner.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.holding_voltage_spinner.setDecimals(3)
        self.holding_voltage_spinner.setMinimum(-100.0)
        self.holding_voltage_spinner.setMaximum(100.0)
        self.holding_voltage_spinner.setSingleStep(0.001)
        self.holding_voltage_spinner.setObjectName(_fromUtf8("holding_voltage_spinner"))
        self.label_26 = QtGui.QLabel(self.frame)
        self.label_26.setGeometry(QtCore.QRect(0, 220, 111, 31))
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.frame_9.raise_()
        self.label_17.raise_()
        self.label_16.raise_()
        self.pulse_length_spinner.raise_()
        self.amplitude_spinner.raise_()
        self.down_spinner_1.raise_()
        self.label_18.raise_()
        self.down_spinner_2.raise_()
        self.label_21.raise_()
        self.commander_scale_spinner.raise_()
        self.label_19.raise_()
        self.frame_7.raise_()
        self.get_commander_scale_button.raise_()
        self.show_wave_button.raise_()
        self.close_window.raise_()
        self.holding_voltage_spinner.raise_()
        self.label_26.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Amplifier Telegraph", None))
        self.label_17.setToolTip(_translate("Dialog", "Length of pulse", None))
        self.label_17.setText(_translate("Dialog", "Pulse Length (s)", None))
        self.label_16.setToolTip(_translate("Dialog", "Length of pre pulse down time", None))
        self.label_16.setText(_translate("Dialog", "Pre Pulse Down \n"
"Time (s)", None))
        self.pulse_length_spinner.setToolTip(_translate("Dialog", "Length of pulse", None))
        self.amplitude_spinner.setToolTip(_translate("Dialog", "Amplitude of voltage step", None))
        self.down_spinner_1.setToolTip(_translate("Dialog", "Length of pre pulse down time", None))
        self.label_18.setToolTip(_translate("Dialog", "Amplitude of voltage step", None))
        self.label_18.setText(_translate("Dialog", "Pulse \n"
"Amplitude (V)", None))
        self.down_spinner_2.setToolTip(_translate("Dialog", "Length of post pulse down time", None))
        self.label_21.setToolTip(_translate("Dialog", "Length of post pulse down time", None))
        self.label_21.setText(_translate("Dialog", "Post Pulse \n"
"Down Time (s)", None))
        self.commander_scale_spinner.setToolTip(_translate("Dialog", "Input scale done by amplifier", None))
        self.label_19.setToolTip(_translate("Dialog", "Input scale done by amplifier", None))
        self.label_19.setText(_translate("Dialog", "Commander \n"
"Scale (mV/V)", None))
        self.frame_7.setToolTip(_translate("Dialog", "Get commander scale from amplifier settings file", None))
        self.get_commander_scale_button.setText(_translate("Dialog", "Get Commander Scale \n"
"From Amplifier Settings", None))
        self.show_wave_button.setToolTip(_translate("Dialog", "Show Waveform", None))
        self.show_wave_button.setText(_translate("Dialog", "Show Waveform", None))
        self.frame_9.setToolTip(_translate("Dialog", "Show Waveform", None))
        self.close_window.setToolTip(_translate("Dialog", "Close the amplifier telegraph editor", None))
        self.close_window.setText(_translate("Dialog", "Close", None))
        self.holding_voltage_spinner.setToolTip(_translate("Dialog", "Input scale done by amplifier", None))
        self.label_26.setToolTip(_translate("Dialog", "Input scale done by amplifier", None))
        self.label_26.setText(_translate("Dialog", "Holding \n"
"Voltage (V)", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


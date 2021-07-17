from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import QRect
from PyQt5.QtCore import Qt

from python.Constants import *
from python.widgets.DonationAddress import DonationAddress
from python.widgets.DonationExitButton import DonationExitButton
from python.widgets.DonationThankYou import DonationThankYou
from python.widgets.DonationTitle import DonationTitle
from python.widgets.DonateLabel import DonateLabel


class DonateFrame(QFrame):
    def __init__(self, frame):
        super().__init__(frame)
        self.setGeometry(QRect(140, 195, 330, 290))
        self.setAutoFillBackground(False)
        self.setFrameShape(QFrame.Box)
        self.setLineWidth(2)
        self.setFrameShadow(QFrame.Raised)
        self.setObjectName(DONATE_FRAME_ID)

        self.title_label = DonationTitle(self)
        self.paypal_label = DonateLabel(self, PAYPAL_LABEL_ID, QRect(20, 90, 130, 30))
        self.bitcoin_label = DonateLabel(self, BITCOIN_LABEL_ID, QRect(20, 160, 130, 30))
        self.eth_label = DonateLabel(self, ETH_LABEL_ID, QRect(20, 230, 130, 30))
        self.eth_address = DonationAddress(self, ETH_ADDRESS_ID, QRect(20, 260, 305, 20))
        self.bitcoin_address = DonationAddress(self, BITCOIN_ADDRESS_ID, QRect(20, 190, 305, 20))
        self.paypal_link = DonationAddress(self, BITCOIN_ADDRESS_ID, QRect(20, 120, 305, 20))

        self.thank_you_label = DonationThankYou(self)
        self.exit_button = DonationExitButton(self)

        self.title_label.setText(DONATION_TITLE)
        self.paypal_label.setText(PAYPAL_LABEL)
        self.bitcoin_label.setText(BITCOIN_LABEL)
        self.eth_label.setText(ETH_LABEL)
        self.eth_address.setText(ETH_ADDRESS)
        self.eth_address.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.bitcoin_address.setText(BITCOIN_ADDRESS)
        self.bitcoin_address.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.paypal_link.setOpenExternalLinks(True)
        self.paypal_link.setText(PAYPAL_ADDRESS)
        self.thank_you_label.setText(THANK_YOU_LABEL)
        self.exit_button.setText("X")

import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label1.Location = System.Drawing.Point(84, 29)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(551, 336)
		self._label1.TabIndex = 0
		self._label1.Text = """My name is Anthony Weitzel and I am 14 years old, I like to play sports and watch them. As an adult I want to become an orthodontist.
"""
		self._label1.Click += self.Label1Click
		# 
		# Form1
		# 
		self.BackColor = System.Drawing.Color.ForestGreen
		self.ClientSize = System.Drawing.Size(742, 374)
		self.Controls.Add(self._label1)
		self.Name = "Form1"
		self.Text = "All about me"
		self.ResumeLayout(False)


	def Label1Click(self, sender, e):
		pass
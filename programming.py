import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button1.Location = System.Drawing.Point(179, 195)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(110, 46)
		self._button1.TabIndex = 1
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button2.Location = System.Drawing.Point(312, 195)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(113, 43)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button3.Location = System.Drawing.Point(445, 195)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(106, 43)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label1.Location = System.Drawing.Point(169, 67)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(382, 112)
		self._label1.TabIndex = 5
		self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(743, 395)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Programming"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)


	def CheckBox1CheckedChanged(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		self._label1.Text = "Hello, world!"

	def Button2Click(self, sender, e):
		self._label1.Text = ""
		

	def MainFormLoad(self, sender, e):
		pass
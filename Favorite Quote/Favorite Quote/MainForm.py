import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(29, 29, 29)
		self._label1.Font = System.Drawing.Font("Perpetua", 36, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(165, 79)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(572, 249)
		self._label1.TabIndex = 0
		self._label1.Text = "To the world you may be one person, but to one person you may be the world."
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(64, 64, 64)
		self._label2.Font = System.Drawing.Font("Perpetua", 36, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(205, 339)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(488, 80)
		self._label2.TabIndex = 1
		self._label2.Text = "Dr. Suess"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(44, 44, 44)
		self.ClientSize = System.Drawing.Size(892, 622)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Favorite Quote"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)


	def Label1Click(self, sender, e):
		pass

	def MainFormLoad(self, sender, e):
		pass
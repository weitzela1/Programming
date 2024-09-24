import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		resources = System.Resources.ResourceManager("My_schedule.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.OliveDrab
		self._label1.Font = System.Drawing.Font("Times New Roman", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(44, 40)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(293, 464)
		self._label1.TabIndex = 0
		self._label1.Text = resources.GetString("label1.Text")
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._label1.Click += self.Label1Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.YellowGreen
		self.ClientSize = System.Drawing.Size(900, 621)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "My schedule"
		self.ResumeLayout(False)


	def Label1Click(self, sender, e):
		pass
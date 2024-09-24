import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.FromArgb(192, 64, 0)
		self._label1.Location = System.Drawing.Point(101, 49)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(721, 532)
		self._label1.TabIndex = 0
		self._label1.Text = "Anthony Joseph Weitzel"
		self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Chocolate
		self.ClientSize = System.Drawing.Size(893, 632)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "My Name"
		self.ResumeLayout(False)


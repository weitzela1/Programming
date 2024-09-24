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
		self._label1.Font = System.Drawing.Font("Nirmala UI", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(169, 31)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(561, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "My favorite club is..."
		self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ButtonShadow
		self._label2.Font = System.Drawing.Font("Modern No. 20", 47.9999962, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(169, 54)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(561, 306)
		self._label2.TabIndex = 1
		self._label2.Text = "Investment Club"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.AppWorkspace
		self.ClientSize = System.Drawing.Size(897, 433)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Favorite Club"
		self.ResumeLayout(False)


	def Label1Click(self, sender, e):
		pass
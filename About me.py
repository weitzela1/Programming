
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form3(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(109, 36)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(691, 109)
		self._label1.TabIndex = 0
		self._label1.Text = "My Favorite Club is ..."
		self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Modern No. 20", 35.9999962, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.SystemColors.MenuHighlight
		self._textBox1.Location = System.Drawing.Point(220, 83)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(465, 59)
		self._textBox1.TabIndex = 1
		self._textBox1.Text = "Investment Club"
		self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# Form3
		# 
		self.BackColor = System.Drawing.Color.LightSlateGray
		self.ClientSize = System.Drawing.Size(900, 590)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "Form3"
		self.Text = "Form3"
		self.ResumeLayout(False)
		self.PerformLayout()


	def TextBox1TextChanged(self, sender, e):
		pass
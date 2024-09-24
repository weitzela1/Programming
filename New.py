
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form2(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.SystemColors.ScrollBar
		self._textBox1.Font = System.Drawing.Font("Segoe Marker", 36, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.SystemColors.MenuHighlight
		self._textBox1.Location = System.Drawing.Point(26, 66)
		self._textBox1.Multiline = True
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(680, 60)
		self._textBox1.TabIndex = 0
		self._textBox1.Text = " Craig Rules!"
		self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# Form
		# 
		self.BackColor = System.Drawing.SystemColors.MenuHighlight
		self.ClientSize = System.Drawing.Size(732, 503)
		self.Controls.Add(self._textBox1)
		self.ForeColor = System.Drawing.SystemColors.ActiveCaption
		self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.Fixed3D
		self.Name = "Form"
		self.Text = "Form2"
		self.Load += self.Form2Load
		self.ResumeLayout(False)
		self.PerformLayout()


	def TextBox1TextChanged(self, sender, e):
		pass

	def Form2Load(self, sender, e):
		pass
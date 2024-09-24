import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.SystemColors.InactiveCaption
		self._textBox1.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(86, 33)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(359, 29)
		self._textBox1.TabIndex = 0
		self._textBox1.Text = "Phone Numbers from my favorite buisnesses:"
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.CadetBlue
		self._label1.Font = System.Drawing.Font("Century", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(84, 77)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(361, 25)
		self._label1.TabIndex = 1
		self._label1.Text = "- Chipotle: (608) 373-0454"
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.CadetBlue
		self._label2.Font = System.Drawing.Font("Century", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(84, 102)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(361, 25)
		self._label2.TabIndex = 2
		self._label2.Text = "- Costco: (779) 513-8397"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.CadetBlue
		self._label3.Font = System.Drawing.Font("Century", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(84, 127)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(361, 25)
		self._label3.TabIndex = 3
		self._label3.Text = """- Citrus Cafe (608) 754-9006

"""
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.CadetBlue
		self._label4.Font = System.Drawing.Font("Century", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(84, 152)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(361, 25)
		self._label4.TabIndex = 4
		self._label4.Text = """- Rotary Gardens: (608) 752-3885
"""
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.CadetBlue
		self._label5.Font = System.Drawing.Font("Century", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(84, 177)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(361, 312)
		self._label5.TabIndex = 5
		self._label5.Text = """- Riversedge Bowl: (608) 756-1201

"""
		self._label5.Click += self.Label5Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.PowderBlue
		self.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
		self.ClientSize = System.Drawing.Size(896, 498)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Phone Numbers"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label1Click(self, sender, e):
		pass

	def Label5Click(self, sender, e):
		pass
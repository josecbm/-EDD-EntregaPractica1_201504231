using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace practica1_edd
{
    public partial class mostrarReporte : Form
    {
        public mostrarReporte()
        {
            InitializeComponent();
            pictureBox1.Image = Image.FromFile(@"C:\Users\jose_\Documents\universidad\segundoSemestre2017\estructuras\practica1\nodoCreado.png");
        }
    }
}

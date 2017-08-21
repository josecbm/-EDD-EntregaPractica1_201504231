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
    public partial class administrarMensajescs : Form
    {
        public administrarMensajescs()
        {
            InitializeComponent();
        }

        private void btnEnviarM_Click(object sender, EventArgs e)
        {
            envioMensaje envio = new envioMensaje();
                envio.Show();
        }

        private void btnRegresar_Click(object sender, EventArgs e)
        {
            Form1 frm2 = new Form1();

            frm2.Show();
            this.Close();
        }

        private void btnCola_Click(object sender, EventArgs e)
        {
            colaMensajes c = new colaMensajes();
            c.Show();
            
        }
    }
}

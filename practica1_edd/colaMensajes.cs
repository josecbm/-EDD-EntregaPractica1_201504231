using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace practica1_edd
{
    public partial class colaMensajes : Form
    {
        public colaMensajes()
        {
            InitializeComponent();
            string fileJSON = File.ReadAllText(@"C:\Users\jose_\Documents\universidad\segundoSemestre2017\estructuras\practica1\datosfinales3.json");
            DataTable dt = (DataTable)JsonConvert.DeserializeObject(fileJSON, typeof(DataTable));
            dataGridView1.DataSource = dt;
            InitializeComponent();
        }
    }
}

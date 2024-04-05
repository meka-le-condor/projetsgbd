const express = require('express');
const Swal = require('sweetalert2');
const mysql = require('mysql2');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(cors());

// Configurer la connexion à la base de données
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'meka',
  password: 'meka',
  database: 'projetsgbd',
});

// Établir la connexion à la base de données
connection.connect((err) => {
  if (err) {
    console.error('Erreur de connexion à la base de données :', err);
  } else {
    console.log('Connecté à la base de données MySQL');
  }
});
 
// Définir une route pour recevoir les données du formulaire
app.post('/api/register', (req, res) => {
  const { email, password, fonction } = req.body;

  // Insérer les données du formulaire dans la base de données
  const query = `INSERT INTO user (email, password, fonction) VALUES (?, ?, ?)`;
  connection.query(query, [email, password, fonction], (err, result) => {
    if (err) {
      console.error('Erreur lors de l\'insertion des données :', err);
      res.status(500).json({ error: 'Une erreur s\'est produite lors de l\'enregistrement des données' });
    } else {
      console.log('Données enregistrées avec succès');
      res.json({ success: true });
    }
  });
});

app.post('/api/etudianteva', (req, res) => {
  const evaform = req.body; // Supposons que vous récupérez les données de l'évaluation à partir de la requête POST

  // Effectuer la requête SQL pour enregistrer les données d'évaluation dans la base de données
  const sqlQuery = `
    INSERT INTO evaluation (module_id, syllabus, objectifs, contenu, support, respect_contenu, volume_horaire, video_projecteur, tableau_noir, materiel_informatique, ponctuel, clair, participation, disponibilite, commentaires)
    VALUES ('${evaform.module_id}', '${evaform.syllabus}', '${evaform.objectifs}', '${evaform.contenu}', '${evaform.support}', '${evaform.respect_contenu}', '${evaform.volume_horaire}', '${evaform.video_projecteur}', '${evaform.tableau_noir}', '${evaform.materiel_informatique}', '${evaform.ponctuel}', '${evaform.clarte_explications}', '${evaform.participation}', '${evaform.disponibilite}', '${evaform.commentaires}');
  `;

  // Exécuter la requête SQL
  connection.query(sqlQuery, (err, result) => {
    if (err) {
      console.error('Erreur lors de l\'insertion des données :', err);
      res.status(500).json({ error: 'Une erreur s\'est produite lors de l\'enregistrement des données' });
    } else {
      console.log('Données enregistrées avec succès');
      res.json({ success: true });
    }
  });
});

app.post('/api/login', (req, res) => {
  const { email, password } = req.body;

  // Vérifier les informations de connexion dans la base de données
  const query = `SELECT * FROM user WHERE email = ? AND password = ?`;
  connection.query(query, [email, password], (err, result) => {
    console.log(password)
    if (err) {
      console.error('Erreur lors de la vérification des informations de connexion :', err);
      res.status(500).json({ error: 'Une erreur s\'est produite lors de la vérification des informations de connexion' });
    } else {
      if (result.length > 0) {
        res.json({ success: true, message: 'Connexion réussie',fonction: result[0].fonction});
          
          res.json({ success: false, message: 'Informations de connexion incorrectes' });
      }else{
       
        console.log('donnee introuvable');
      } 
    }
  });
}); 

//recuperer les donnee de module
app.get('/data',(req,res)=>{

  const sqlquery= `SELECT * FROM module`;
  
  connection.query(sqlquery,(err,result)=>{
    console.log(result);
    if(result.length>0){
      res.json({ success : true ,message:'' ,  data:result})


    }else{
      err.json(()=>{console.log('data not found')})

    }

  })
  
  

})

// Lancer le serveur
const port = 3000; // Remplacez par le port de votre choix
app.listen(port, () => {
  console.log(`Serveur démarré sur le port ${port}`);
});
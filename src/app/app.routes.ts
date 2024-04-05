import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { EnseignementComponent } from './enseignement/enseignement.component';
import { RouterModule, Routes } from '@angular/router';
import { EtudiantComponent } from './etudiant/etudiant.component';
import { EnseignantComponent } from './enseignant/enseignant.component';
import { AcceuilComponent } from './acceuil/acceuil.component';
import { ConnexionComponent } from './connexion/connexion.component';
import { InscriptionComponent } from './inscription/inscription.component';


export const routes: Routes = [  {path: '', redirectTo :'Acceuil', pathMatch :'full'},
    {path: 'Acceuil', component :AcceuilComponent},
    {path: 'Connexion', component :ConnexionComponent},
    {path: 'Inscription', component :InscriptionComponent},
    {path: 'etudiant', component :EtudiantComponent},
    {path: 'enseignant', component :EnseignantComponent},
    {path: 'enseignement', component :EnseignementComponent},
  
  ];
 
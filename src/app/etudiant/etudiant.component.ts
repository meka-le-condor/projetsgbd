import { Component } from '@angular/core';
import { RouterOutlet,Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators,FormsModule, NgForm } from '@angular/forms';
import Swal from 'sweetalert2';
import axios from 'axios';
import { User ,Evaluation} from '../User';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-etudiant',
  standalone: true,
  imports: [RouterOutlet,FormsModule],
  templateUrl: './etudiant.component.html',
  styleUrl: './etudiant.component.css'
})
export class EtudiantComponent {
  title='GEE';
  public evaluation: Evaluation = new Evaluation();


  public submitForm(evaform: NgForm) {
    if (evaform.valid) {
      const formData = evaform.value;
      console.log(formData)
      axios.post('http://localhost:3000/api/etudianteva', formData)
        .then(response => {
      
          Swal.fire('Succès', 'Login réussi !', 'success');
        
  
          evaform.reset();
        })
        .catch(error => {
          Swal.fire('Erreur', 'Erreur ', 'error');
          console.error('Erreur lors de la connexion', error);
        });
    }
  }
}

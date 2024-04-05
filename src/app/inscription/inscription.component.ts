import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators,FormsModule, NgForm } from '@angular/forms';
import axios from 'axios';
import { User } from '../User';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-inscription',
  standalone: true,
  templateUrl: './inscription.component.html',
  imports: [FormsModule],
  styleUrls: ['./inscription.component.css']
})
export class InscriptionComponent {
  title= 'GEE';

    public user:User = new User();

 

  public submitForm(registerform:NgForm) {

    if (registerform.valid) {
      const FormData = registerform.value;
      console.log("hello");
      axios.post('http://localhost:3000/api/register',FormData)
        .then(response => {
          Swal.fire('Succès', 'Enregistrement réussi !', 'success');
          console.log('Enregistrement réussi !', response.data);
          
          registerform.reset();
        })
        .catch(error => {
          Swal.fire('Erreur', 'Erreur lors de l\'enregistrement', 'error');
          console.error('Erreur lors de l\'enregistrement', error);
        });
    }
    
  }
}
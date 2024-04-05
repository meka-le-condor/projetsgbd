import { Component } from '@angular/core';
import { Router , RouterOutlet} from '@angular/router';
import { FormBuilder, FormGroup, Validators,FormsModule, NgForm } from '@angular/forms';
import Swal from 'sweetalert2';
import axios from 'axios';
import { User } from '../User';
@Component({
  selector: 'app-connexion',
  standalone: true,
  imports: [RouterOutlet,FormsModule],
  templateUrl: './connexion.component.html',
  styleUrl: './connexion.component.css'
  })
export class ConnexionComponent {title = 'GEE';
  public user: User = new User();

  constructor(private router: Router) {}

  public submitForm(loginForm: NgForm) {
    if (loginForm.valid) {
      const formData = loginForm.value;
  
      axios.post('http://localhost:3000/api/login', formData)
        .then(response => {
          const status = response.data.fonction; // Récupérer la fonction depuis response.data
        
          Swal.fire('Succès', 'Login réussi !', 'success');
        
  
          if(status === 'Etudiant'){this.router.navigate(['/etudiant']);}
          if(status === 'Enseignant'){this.router.navigate(['/enseignant']);}
            
           
  
          loginForm.reset();
        })
        .catch(error => {
          Swal.fire('Erreur', 'Erreur AUTHENTIFICATION', 'error');
          console.error('Erreur lors de la connexion', error);
        });
    }
  }
}
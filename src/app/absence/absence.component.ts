import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import axios from 'axios';
import { absence} from '../User';
import { NgForOf, NgIf } from '@angular/common';
import { FormsModule , NgForm} from '@angular/forms';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-absence',  standalone: true,
  templateUrl: './absence.component.html',
  imports: [RouterOutlet,FormsModule,NgForOf,NgIf],
  styleUrls: ['./absence.component.css']
})
export class AbsenceComponent {
 title='Absence'; 
  public absence: absence = new absence();
 public submitForm(abs:NgForm){

  if (abs.valid) {
    const formDataa = abs.value;
    console.log(formDataa)
    axios.post('http://localhost:3000/absence', formDataa)
      .then(response => {
    
        Swal.fire('Succès', 'Donnee Enrregistrer !', 'success');
      

        abs.reset();
      })
      .catch(error => {
        Swal.fire('Erreur', 'Erreur enregistrement ', 'error');
        console.error('Erreur lors de lenregistrement', error);
      });
    }
  }

  data: any;

          
  ngOnInit(): void {
    axios.get('http://localhost:3000/data/absence')
    .then(response => {
      this.data = response.data.data;
     
    })
    .catch(error => {
      console.error(error);
    });
}
selectedItem: any;

openDetails(item: any) {
  this.selectedItem = item;
}

closeDetails() {
  this.selectedItem = null;
}
}

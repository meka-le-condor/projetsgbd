import { Component } from '@angular/core';
import { FormsModule, NgForm } from '@angular/forms';
import { RouterOutlet } from '@angular/router';
import Swal from 'sweetalert2';
import axios from 'axios';
import { Cahierdetext} from '../User';
import { NgForOf, NgIf } from '@angular/common';

@Component({
  selector: 'app-cahiertext',  standalone: true,
  templateUrl: './cahiertext.component.html',
  imports: [RouterOutlet,FormsModule,NgForOf,NgIf],
  styleUrls: ['./cahiertext.component.css']
})
export class CahiertextComponent {
  title= 'Cahierdetexte';
  public cahierdetext: Cahierdetext = new Cahierdetext();

  public submitForm(cdt:NgForm){

    if (cdt.valid) {
      const formData = cdt.value;
      console.log(formData)
      axios.post('http://localhost:3000/api/cdt', formData)
        .then(response => {
      
          Swal.fire('Succès', 'Donnee Enrregistrer !', 'success');
        
  
          cdt.reset();
        })
        .catch(error => {
          Swal.fire('Erreur', 'Erreur enregistrement ', 'error');
          console.error('Erreur lors de lenregistrement', error);
        });
      }
    }

    data: any;

            
    ngOnInit(): void {
      axios.get('http://localhost:3000/cdt')
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
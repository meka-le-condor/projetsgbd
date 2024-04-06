import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import Swal from 'sweetalert2';
import axios from 'axios';
import { Evaluation} from '../User';
import { NgForOf, NgIf } from '@angular/common';
import { FormsModule } from '@angular/forms';
@Component({
  selector: 'app-suivievaluation',standalone: true,
  templateUrl: './suivievaluation.component.html',
  imports: [RouterOutlet,FormsModule,NgForOf,NgIf],
  styleUrls: ['./suivievaluation.component.css']
})
export class SuivievaluationComponent {
  title='suivi';

  data: any;datam: any;

            
    ngOnInit(): void {
      axios.get('http://localhost:3000/eva')
      .then(response => {
        this.data = response.data.data;
        this.datam = response.data.datam;

       
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


export class User {
    public email!: string;
    public password!: string;
    public fonction!: string;
  }
  
  export class Evaluation {
    public module_id!: number;
    public syllabus!: string;
    public objectifs!: string;
    public contenu!: string;
    public support!: string;
    public respect_contenu!: string;
    public volume_horaire!: string;
    public video_projecteur!: string;
    public tableau_noir!: string;
    public materiel_informatique!: string;
    public ponctuel!: string;
    public clair!: string;
    public competences_pedagogiques!:string;
    public participation!: string;
    public disponibilite!: string;
    public clarte_explications!: string;
    public commentaires!: string;
  }
  export class Cahierdetext {
    date!: string;
    matiere!: string;
    enseignant!: string;
    activite1!: string;
    activite2!: string;
    activite3!: string;
    remarques!: string;
    classe!: string;
  }
  export class absence {
    date!: string;
    module!: string;
    enseignant!: string;
    classe!: string;
    eleves!: string;
   
  }
import tkinter as tk
from tkinter import messagebox, ttk

from bibliotheque import Bibliotheque
from livre import Livre
from film import Film
from musique import Musique

class InterfaceBibliotheque(tk.Tk):
    def __init__(self):
        super().__init__()

        self.biblio = Bibliotheque()
        self.biblio.charger("medias.json")

        self.title("\U0001F4DA Bibliothèque Multimédia")
        self.geometry("700x450")
        self.configure(bg="#c471ed")

        title_label = tk.Label(self, text="Bibliothèque Multimédia", 
                               font=("Arial", 20, "bold"), fg="white", bg="#c471ed")
        title_label.pack(pady=10)

        frame_list = tk.Frame(self, bg="#d16ba5")
        frame_list.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        self.listbox = tk.Listbox(frame_list, bg="#ecf0f1", fg="#2c3e50",
                                  font=("Arial", 12), selectbackground="#a1459c")
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame_list, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

        frame_buttons = tk.Frame(self, bg="#c471ed")
        frame_buttons.pack(pady=10)

        tk.Button(frame_buttons, text="➕ Ajouter", command=self.ouvrir_ajouter,
                  bg="#d16ba5", fg="white", font=("Arial", 12, "bold"), width=18).grid(row=0, column=0, padx=10)

        tk.Button(frame_buttons, text="🔍 Rechercher", command=self.ouvrir_rechercher,
                  bg="#a1459c", fg="white", font=("Arial", 12, "bold"), width=18).grid(row=0, column=1, padx=10)

        tk.Button(frame_buttons, text="❌ Supprimer par titre", command=self.ouvrir_supprimer,
                  bg="#9b59b6", fg="white", font=("Arial", 12, "bold"), width=20).grid(row=0, column=2, padx=10)

        tk.Button(frame_buttons, text="📄 Afficher tout", command=self.afficher_tout,
                  bg="#8e44ad", fg="white", font=("Arial", 12, "bold"), width=18).grid(row=0, column=3, padx=10)

        self.afficher_tout()

    def afficher_tout(self):
        self.listbox.delete(0, tk.END)
        for media in self.biblio.medias:
            self.listbox.insert(tk.END, media.afficher())

    def ouvrir_ajouter(self):
        self.listbox.delete(0, tk.END)
        self.fenetre_ajout = tk.Toplevel(self)
        self.fenetre_ajout.title("Ajouter un média")
        self.fenetre_ajout.geometry("400x350")
        self.fenetre_ajout.configure(bg="#d16ba5")
        self.fenetre_ajout.grab_set()

        tk.Label(self.fenetre_ajout, text="Choisir le type de média :", 
                 bg="#d16ba5", fg="white", font=("Arial", 14)).pack(pady=10)

        self.type_var = tk.StringVar(value="Livre")

        for t in ["Livre", "Film", "Musique"]:
            tk.Radiobutton(self.fenetre_ajout, text=t, variable=self.type_var, value=t, 
                           bg="#d16ba5", fg="white", selectcolor="#a1459c", font=("Arial", 12),
                           command=self.afficher_formulaire).pack(anchor=tk.W, padx=20)

        self.form_frame = tk.Frame(self.fenetre_ajout, bg="#d16ba5")
        self.form_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.afficher_formulaire()

        btn_frame = tk.Frame(self.fenetre_ajout, bg="#d16ba5")
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Ajouter", command=self.ajouter_media,
                  bg="#27ae60", fg="white", font=("Arial", 11, "bold"), width=10).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Annuler", command=self.fenetre_ajout.destroy,
                  bg="#c0392b", fg="white", font=("Arial", 11, "bold"), width=10).grid(row=0, column=1, padx=10)

    def afficher_formulaire(self):
        for widget in self.form_frame.winfo_children():
            widget.destroy()

        tk.Label(self.form_frame, text="Titre :", bg="#d16ba5", fg="white").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_titre = tk.Entry(self.form_frame, width=30)
        self.entry_titre.grid(row=0, column=1, pady=5)

        tk.Label(self.form_frame, text="Année :", bg="#d16ba5", fg="white").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_annee = tk.Entry(self.form_frame, width=30)
        self.entry_annee.grid(row=1, column=1, pady=5)

        t = self.type_var.get()
        if t == "Livre":
            tk.Label(self.form_frame, text="Auteur :", bg="#d16ba5", fg="white").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
            self.entry_auteur = tk.Entry(self.form_frame, width=30)
            self.entry_auteur.grid(row=2, column=1, pady=5)

            tk.Label(self.form_frame, text="Nombre de pages :", bg="#d16ba5", fg="white").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
            self.entry_nb_pages = tk.Entry(self.form_frame, width=30)
            self.entry_nb_pages.grid(row=3, column=1, pady=5)

        elif t == "Film":
            tk.Label(self.form_frame, text="Réalisateur :", bg="#d16ba5", fg="white").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
            self.entry_realisateur = tk.Entry(self.form_frame, width=30)
            self.entry_realisateur.grid(row=2, column=1, pady=5)

            tk.Label(self.form_frame, text="Durée (min) :", bg="#d16ba5", fg="white").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
            self.entry_duree = tk.Entry(self.form_frame, width=30)
            self.entry_duree.grid(row=3, column=1, pady=5)

        elif t == "Musique":
            tk.Label(self.form_frame, text="Artiste :", bg="#d16ba5", fg="white").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
            self.entry_artiste = tk.Entry(self.form_frame, width=30)
            self.entry_artiste.grid(row=2, column=1, pady=5)

            tk.Label(self.form_frame, text="Genre :", bg="#d16ba5", fg="white").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
            self.entry_genre = tk.Entry(self.form_frame, width=30)
            self.entry_genre.grid(row=3, column=1, pady=5)

    def ajouter_media(self):
        t = self.type_var.get()
        titre = self.entry_titre.get().strip()
        annee = self.entry_annee.get().strip()

        if not titre or not annee.isdigit():
            messagebox.showerror("Erreur", "Titre et année valides sont obligatoires.")
            return

        annee = int(annee)

        try:
            if t == "Livre":
                auteur = self.entry_auteur.get().strip()
                nb_pages = self.entry_nb_pages.get().strip()
                if not auteur or not nb_pages.isdigit():
                    raise ValueError("Auteur et nombre de pages valides sont obligatoires.")
                nb_pages = int(nb_pages)
                media = Livre(titre, annee, auteur, nb_pages)

            elif t == "Film":
                realisateur = self.entry_realisateur.get().strip()
                duree = self.entry_duree.get().strip()
                if not realisateur or not duree.isdigit():
                    raise ValueError("Réalisateur et durée valides sont obligatoires.")
                duree = int(duree)
                media = Film(titre, annee, realisateur, duree)

            elif t == "Musique":
                artiste = self.entry_artiste.get().strip()
                genre = self.entry_genre.get().strip()
                if not artiste or not genre:
                    raise ValueError("Artiste et genre sont obligatoires.")
                media = Musique(titre, annee, artiste, genre)

            self.biblio.ajouter(media)
            self.biblio.sauvegarder("medias.json")

            messagebox.showinfo("Succès", f"{t} ajouté avec succès.")
            self.fenetre_ajout.destroy()
            self.afficher_tout()

        except ValueError as e:
            messagebox.showerror("Erreur", str(e))

    def ouvrir_rechercher(self):
        self.listbox.delete(0, tk.END)
        self.fenetre_recherche = tk.Toplevel(self)
        self.fenetre_recherche.title("Rechercher un média")
        self.fenetre_recherche.geometry("350x150")
        self.fenetre_recherche.configure(bg="#d16ba5")
        self.fenetre_recherche.grab_set()

        tk.Label(self.fenetre_recherche, text="Titre à rechercher :", bg="#d16ba5", fg="white", font=("Arial", 12)).pack(pady=10)
        self.entry_recherche = tk.Entry(self.fenetre_recherche, width=30)
        self.entry_recherche.pack(pady=5)

        btn_frame = tk.Frame(self.fenetre_recherche, bg="#d16ba5")
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Rechercher", command=self.rechercher,
                  bg="#a1459c", fg="white", font=("Arial", 11, "bold"), width=10).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Annuler", command=self.fenetre_recherche.destroy,
                  bg="#c0392b", fg="white", font=("Arial", 11, "bold"), width=10).grid(row=0, column=1, padx=10)

    def rechercher(self):
        recherche = self.entry_recherche.get().strip()
        if not recherche:
            messagebox.showwarning("Attention", "Entrez un titre à rechercher.")
            return

        resultats = self.biblio.rechercher(recherche)

        self.listbox.delete(0, tk.END)
        if resultats:
            for i, m in enumerate(resultats):
                self.listbox.insert(tk.END, m.afficher())
                self.listbox.itemconfig(i, {'bg': '#f9e79f'})
            self.fenetre_recherche.destroy()
        else:
            messagebox.showinfo("Résultat", "Aucun média trouvé.")

    def ouvrir_supprimer(self):
        self.listbox.delete(0, tk.END)
        self.fenetre_supprimer = tk.Toplevel(self)
        self.fenetre_supprimer.title("Supprimer un média")
        self.fenetre_supprimer.geometry("350x150")
        self.fenetre_supprimer.configure(bg="#d16ba5")
        self.fenetre_supprimer.grab_set()

        tk.Label(self.fenetre_supprimer, text="Titre du média à supprimer :", bg="#d16ba5", fg="white", font=("Arial", 12)).pack(pady=10)
        self.entry_supprimer = tk.Entry(self.fenetre_supprimer, width=30)
        self.entry_supprimer.pack(pady=5)

        btn_frame = tk.Frame(self.fenetre_supprimer, bg="#d16ba5")
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Supprimer", command=self.supprimer_media,
                  bg="#9b59b6", fg="white", font=("Arial", 11, "bold"), width=10).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Annuler", command=self.fenetre_supprimer.destroy,
                  bg="#c0392b", fg="white", font=("Arial", 11, "bold"), width=10).grid(row=0, column=1, padx=10)

    def supprimer_media(self):
        titre = self.entry_supprimer.get().strip()
        if not titre:
            messagebox.showwarning("Attention", "Entrez un titre à supprimer.")
            return

        resultats = self.biblio.rechercher(titre)
        if not resultats:
            messagebox.showinfo("Résultat", "Aucun média trouvé avec ce titre.")
            return

        self.listbox.delete(0, tk.END)
        for i, media in enumerate(resultats):
            self.listbox.insert(tk.END, media.afficher())
            self.listbox.itemconfig(i, {'bg': '#f5b7b1'})

        confirm = messagebox.askyesno("Confirmation", f"Supprimer {len(resultats)} média(s) ?")
        if confirm:
            for media in resultats:
                self.biblio.supprimer(media)
            self.biblio.sauvegarder("medias.json")
            messagebox.showinfo("Succès", f"{len(resultats)} média(s) supprimé(s).")
            self.afficher_tout()

        self.fenetre_supprimer.destroy()

if __name__ == "__main__":
    app = InterfaceBibliotheque()
    app.mainloop()

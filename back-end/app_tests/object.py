
# Right format
min_right_quiz_obj = {                                     
  "catégorie-nom-slogan": {
    "en": {
      "catégorie": "Web",
      "nom": "Web apps",
      "slogan": "Computing made easy"
    },
  },
  "quizz": {
      "fr": { "débutant": [{},], "confirmé": [{},], "expert": [{},]},
      "en": { "débutant": [{},], "confirmé": [{},], "expert": [{},]},
      "es": { "débutant": [{},], "confirmé": [{},], "expert": [{},]},
    }
} 

# Bad meta format
bad_metas = {
    'Not a valid python dict' : "", # when isn't a valid python dict
    "catégorie-nom-slogan,en" : {     
        # Bad meta key : Missing "nom" in catégorie-nom-slogan                              
        "catégorie--slogan": {
            "en": {
            "catégorie": "Web",
            "nom": "Web apps",
            "slogan": "Computing made easy"
            },
        },
    },
    "catégorie-nom-slogan,en" : {
        "catégorie-nom-slogan": {
            "": { # Bad base lang code : Missing base languge code "en" 
            "catégorie": "Web",
            "nom": "Web apps",
            "slogan": "Computing made easy"
            },
        },
    },
    "catégorie" : {                     
        "catégorie-nom-slogan": {
            "en": {
            "catégoie": "Web", # Bad key => "categorie" instead of "catégoie"
            "nom": "Web apps",
            "slogan": "Computing made easy"
            },
        },
    }
}

bad_datas = {
    "quizz" : {                                     
        "catégorie-nom-slogan": {
            "en": {
            "catégorie": "Web",
            "nom": "Web apps",
            "slogan": "Computing made easy"
            },
        },
        "quiz": { # Bad data key : "quizz" instead of "quiz" 
        }
    },

    "fr" : {                                     
        "catégorie-nom-slogan": {
            "en": {
            "catégorie": "Web",
            "nom": "Web apps",
            "slogan": "Computing made easy"
            },
        },
        "quizz": { "" : {"débutant": [{}]}} # Missing "fr" quizs  
    }, 

    "en" : {                                     
        "catégorie-nom-slogan": {
            "en": {
            "catégorie": "Web",
            "nom": "Web apps",
            "slogan": "Computing made easy"
            },
        },
        "quizz": { 
            "fr" : {"débutant": [{}], "confirmé": [{}],  "expert": [{}]},
            "" : {"débutant": [{}], "confirmé": [{}],  "expert": [{}]}, # Missing "en" quizs
        }
    }, 

    "es" : {                                     
        "catégorie-nom-slogan": {
            "en": {
            "catégorie": "Web",
            "nom": "Web apps",
            "slogan": "Computing made easy"
            },
        },
        "quizz": { 
            "fr" : {"débutant": [{}], "confirmé": [{}],  "expert": [{}]},
            "en" : {"débutant": [{}], "confirmé": [{}],  "expert": [{}]},
            "" : {"débutant": [{}], "confirmé": [{}],  "expert": [{}]}, # Missing "es" quizs
        }
    },
    
    "débutant" : {                                     
        "catégorie-nom-slogan": {
            "en": {
            "catégorie": "Web",
            "nom": "Web apps",
            "slogan": "Computing made easy"
            },
        },
        "quizz": { 
            # Bad data key : "débuant" instead of "débutant" 
            "fr" : {"débuant": [{}], "confirmé": [{}],  "expert": [{}]},
        }
    },

    "confirmé" : {                                     
        "catégorie-nom-slogan": {
            "en": {
            "catégorie": "Web",
            "nom": "Web apps",
            "slogan": "Computing made easy"
            },
        },
        "quizz": { 
            # Bad data key : "confrmé" instead of "confirmé" 
            "fr" : {"débutant": [{}], "confrmé": [{}],  "expert": [{}]},
        }
    },

    "expert" : {                                     
        "catégorie-nom-slogan": {
            "en": {
            "catégorie": "Web",
            "nom": "Web apps",
            "slogan": "Computing made easy"
            },
        },
        "quizz": { 
            # Bad data key : "exert" instead of "expert" 
            "fr" : {"débutant": [{}], "confirmé": [{}],  "exert": [{}]},
        }
    },
}


# Response sample
resp_s = {                                     
  "fournisseur": "OpenQuizzDB - Fournisseur de contenu libre (https://www.openquizzdb.org)",
  "rédacteur": "Philippe Bresoux",       
  "difficulté": "2 / 5",
  "version": 1,
  "mise-à-jour": "2023-06-19",
  "catégorie-nom-slogan": {
    "fr": {
      "catégorie": "Web",
      "nom": "Applications web",
      "slogan": "L'informatique simplifiée"
    },
    "en": {
      "catégorie": "Web",
      "nom": "Web apps",
      "slogan": "Computing made easy"
    },
    "es": {
      "catégorie": "Web",
      "nom": "Aplicaciones web",
      "slogan": "Informática simplificada"
    },
    "it": {
      "catégorie": "Ragnatela",
      "nom": "App web",
      "slogan": "Il calcolo semplificato"
    },
    "de": {
      "catégorie": "Netz",
      "nom": "Web-Apps",
      "slogan": "Rechnen leicht gemacht"
    },
    "nl": {
      "catégorie": "Web",
      "nom": "Web-apps",
      "slogan": "Eenvoudig computeren"
    }
  },
  "quizz": {
    "fr": {
      "débutant": [
      {
        "id": 1,
        "question": "Quel logiciel de traitement de texte a été mis au point par la société Microsoft ?",
        "propositions": [
          "Excel",
          "PowerPoint",
          "Access",
          "Word"
        ],
        "réponse": "Word",
        "anecdote": "Microsoft a déjà publié plusieurs logiciels de traitement de texte, mais « Word » en reste la « vedette »."
      },
      {
        "id": 2,
        "question": "Le logiciel « Excel », extrait de la suite bureautique Microsoft Office, est un...",
        "propositions": [
          "Messagerie",
          "Traitement de texte",
          "Tableur",
          "Navigateur internet"
        ],
        "réponse": "Tableur",
        "anecdote": "Excel a été plusieurs fois critiqué pour ses problèmes de précision sur calculs à virgule flottante."
      },
      {
        "id": 3,
        "question": "En informatique, comment appelle-t-on une erreur de programmation encore non localisée ?",
        "propositions": [
          "Virus",
          "Bug",
          "Spam",
          "Crack"
        ],
        "réponse": "Bug",
        "anecdote": "La gravité d'un dysfonctionnement informatique peut aller de bénigne à majeure."
      },
      {
        "id": 4,
        "question": "Quelle version de Windows Microsoft a-t-il lancée le vendredi 26 octobre 2012 ?",
        "propositions": [
          "Windows 8",
          "Windows CE",
          "Windows 7",
          "Windows Mobile"
        ],
        "réponse": "Windows 8",
        "anecdote": "La version de Windows 8.1 est une mise à jour gratuite de Windows 8, disponible depuis 2013."
      },
      {
        "id": 5,
        "question": "Comment est communément abrégée la publication assistée par ordinateur ?",
        "propositions": [
          "USB",
          "VGA",
          "PAO",
          "CIO"
        ],
        "réponse": "PAO",
        "anecdote": "La PAO consiste à créer des documents imprimés en travaillant la composition et la typographie de documents."
      },
      {
        "id": 6,
        "question": "Quelle application informatique de la société Apple permet de gérer facilement un iPod ?",
        "propositions": [
          "HyperCard",
          "QuickTime",
          "iTunes",
          "FileMaker"
        ],
        "réponse": "iTunes",
        "anecdote": "« iTunes » faisait partie de la suite logicielle d'Apple « iLife » jusqu'à la version '06."
      },
      {
        "id": 7,
        "question": "En informatique, quel logiciel permet de créer des calculs automatiques ?",
        "propositions": [
          "Tableur",
          "Débogueur",
          "Navigateur",
          "Explorateur"
        ],
        "réponse": "Tableur",
        "anecdote": "Une feuille de calcul est une table d'informations, la plupart du temps financières."
      },
      {
        "id": 8,
        "question": "Quel pirate informatique casse les systèmes informatiques et les logiciels protégés ?",
        "propositions": [
          "Blagueur",
          "Hacker",
          "Forceur",
          "Pirateur"
        ],
        "réponse": "Hacker",
        "anecdote": "Certains utilisent ce savoir-faire dans un cadre légal, d'autres étant le plus souvent hors-la-loi."
      },
      {
        "id": 9,
        "question": "Quels logiciels permettent de surfer sur Internet, sur PC, tablette ou smartphone ?",
        "propositions": [
          "Tableurs",
          "Émulateurs",
          "Navigateurs",
          "Éditeurs"
        ],
        "réponse": "Navigateurs",
        "anecdote": "Le premier navigateur stable et largement diffusé fut « NCSA Mosaic », en 1993."
      },
      {
        "id": 10,
        "question": "Quel outil développé par le géant Google permet de gérer son emploi du temps ?",
        "propositions": [
          "Google Tempo",
          "Google TimeLine",
          "Google Mobile",
          "Google Agenda"
        ],
        "réponse": "Google Agenda",
        "anecdote": "« Google Agenda » permet de partager des événements et des agendas et de les publier sur internet ou sur un site Web."
      }
    ],
    "confirmé": [
      {
        "id": 11,
        "question": "Quelle grande société a reçu le feu vert en  2011 pour le rachat de « Skype » ?",
        "propositions": [
          "Facebook",
          "Microsoft",
          "Google",
          "Apple"
        ],
        "réponse": "Microsoft",
        "anecdote": "« Skype » est un logiciel gratuit qui permet de passer des appels téléphoniques et vidéo via Internet, ainsi que le partage d'écran."
      },
      {
        "id": 12,
        "question": "Quel est probablement le plus connu des systèmes informatiques dits libres ?",
        "propositions": [
          "Lamento",
          "Lama",
          "Links",
          "Linux"
        ],
        "réponse": "Linux",
        "anecdote": "Linux est un système informatique qui fonctionne sur du matériel allant du téléphone portable au supercalculateur."
      },
      {
        "id": 13,
        "question": "Quelle est le nom de la solution professionnelle de services Google ?",
        "propositions": [
          "Google Pro",
          "Google Mac",
          "Google Apps",
          "Google Serve"
        ],
        "réponse": "Google Apps",
        "anecdote": "Ce site Web au service des entreprises met en ligne de nombreuses applications."
      },
      {
        "id": 14,
        "question": "Quel type de logiciel est mis gratuitement et librement à disposition par son créateur ?",
        "propositions": [
          "Software",
          "Freeware",
          "Adware",
          "Malware"
        ],
        "réponse": "Freeware",
        "anecdote": "Il ne faut toutefois pas confondre freeware (gratuiciel) et shareware (partagiciel)."
      },
      {
        "id": 15,
        "question": "En avril 2012, quelle start-up Facebook a-t-il rachetée pour plus d'un milliard de dollars ?",
        "propositions": [
          "Backelite",
          "Instagram",
          "Globalnet",
          "Valve"
        ],
        "réponse": "Instagram",
        "anecdote": "« Instagram » est une application  co-fondée et lancée par l'américain Kevin Systrom et le Brésilien Michel Mike Krieger en octobre 2010."
      },
      {
        "id": 16,
        "question": "Au Québec, quel mot est souvent utilisé pour désigner le courrier électronique ?",
        "propositions": [
          "Copitel",
          "Courriel",
          "Lettrinter",
          "Emel"
        ],
        "réponse": "Courriel",
        "anecdote": "Le courriel tend à être reconnu comme moyen valide de contacter une personne."
      },
      {
        "id": 17,
        "question": "Quel logiciel racheté par Microsoft a remplacé « Windows Live Messenger » en 2013 ?",
        "propositions": [
          "Skype",
          "Instagram",
          "QuickTime",
          "Pidgin"
        ],
        "réponse": "Skype",
        "anecdote": "« Skype » a été fondé en Estonie par Niklas Zennström et Janus Friis en 2003 et développé par trois Estoniens à l'origine du logiciel « KaZaA »."
      },
      {
        "id": 18,
        "question": "Quel nom portait le précédent navigateur Internet devenu « Microsoft Edge » ?",
        "propositions": [
          "Safari",
          "Firefox",
          "Chrome",
          "Internet Explorer"
        ],
        "réponse": "Internet Explorer",
        "anecdote": "La version 11 du navigateur « Internet Explorer » sera toujours présente dans Windows 10 avant le passage progressif à « Microsoft Edge »."
      },
      {
        "id": 19,
        "question": "Quel logiciel est indispensable pour protéger votre ordinateur sur Internet ?",
        "propositions": [
          "Navigateur",
          "Antivirus",
          "Messagerie",
          "Chat"
        ],
        "réponse": "Antivirus",
        "anecdote": "Les antivirus peuvent balayer le contenu d'un disque dur ainsi que la mémoire vive de l'ordinateur."
      },
      {
        "id": 20,
        "question": "Qui est le tout premier pape à avoir envoyé un message sur « Twitter » ?",
        "propositions": [
          "Benoît XVI",
          "Jean-Paul II",
          "François",
          "Paul VI"
        ],
        "réponse": "Benoît XVI",
        "anecdote": "Réputé conservateur, le cardinal Ratzinger a été élu le 19 avril 2005 pour succéder à Jean-Paul II."
      }
    ],
    "expert": [
      {
        "id": 21,
        "question": "Quel courrielleur créé par Mozilla est le compagnon idéal du navigateur « Firefox » ?",
        "propositions": [
          "Sylpheed",
          "Incredimail",
          "Foxmail",
          "Thunderbird"
        ],
        "réponse": "Thunderbird",
        "anecdote": "Tout comme « Firefox », « Thunderbird » et son interface en XUL est basé sur le moteur Gecko."
      },
      {
        "id": 22,
        "question": "Quel nom porte la suite bureautique en ligne proposée par Microsoft ?",
        "propositions": [
          "StarOffice",
          "Office 365",
          "KOffice",
          "OpenOffice"
        ],
        "réponse": "Office 365",
        "anecdote": "Les abonnements « Office 365 » pour les particuliers permettent de bénéficier de la version complète de la suite Office que l'on connaît."
      },
      {
        "id": 23,
        "question": "Quel était le nom de code de la version 3.1 de Microsoft Windows ?",
        "propositions": [
          "Java",
          "Joke",
          "Jumpman",
          "Janus"
        ],
        "réponse": "Janus",
        "anecdote": "La version 3 a été la première à connaître un large succès, permettant à Microsoft de rivaliser avec l'Apple Macintosh."
      },
      {
        "id": 24,
        "question": "Quel nom porte le service de stockage en ligne de Windows Live ?",
        "propositions": [
          "Dropbox",
          "MediaFire",
          "RapidShare",
          "Onedrive"
        ],
        "réponse": "Onedrive",
        "anecdote": "Ce service en ligne de stockage et d'applications, créé en 2007, est une manifestation du concept de cloud computing."
      },
      {
        "id": 25,
        "question": "Quel est le nouveau nom du logiciel gratuit de messagerie instantanée « Gaim » ?",
        "propositions": [
          "iShare",
          "Connect",
          "Komunity",
          "Pidgin"
        ],
        "réponse": "Pidgin",
        "anecdote": "« Gaim » a été renommé en « Pidgin » en 2007 en raison de plaintes de la société AOL et de sa marque AIM."
      },
      {
        "id": 26,
        "question": "Quelle suite logicielle équivaut à Microsoft Office chez le géant Google ?",
        "propositions": [
          "Google Sites",
          "OpenOffice",
          "Works",
          "Google Documents"
        ],
        "réponse": "Google Documents",
        "anecdote": "« Google Documents » est une suite des évolutions de « Google Spreadsheets » et de « Writely », logiciel de traitement de texte."
      },
      {
        "id": 27,
        "question": "De quel pays la suite logicielle gratuite « Opera » est-elle originaire ?",
        "propositions": [
          "Norvège",
          "France",
          "Italie",
          "Autriche"
        ],
        "réponse": "Norvège",
        "anecdote": "« Opera » est un navigateur Web développé par la société norvégienne Opera Software, qui propose plusieurs logiciels relatifs à Internet."
      },
      {
        "id": 28,
        "question": "Lequel de ces outils ne permet pas de visionner des pages web ?",
        "propositions": [
          "Mozilla Firefox",
          "Google Chrome",
          "Acrobat Reader",
          "Internet Explorer"
        ],
        "réponse": "Acrobat Reader",
        "anecdote": "Adobe change régulièrement le nom des produits de la famille Acrobat et cela en subdivisant sa gamme."
      },
      {
        "id": 29,
        "question": "Combien de téléchargements dénombrait-on sur le célèbre « App Store » fin 2012 ?",
        "propositions": [
          "25 milliards",
          "15 milliards",
          "35 milliards",
          "5 milliards"
        ],
        "réponse": "35 milliards",
        "anecdote": "Depuis la mise à jour du système d'exploitation d'Apple iOS 7 en septembre 2013, l'« App Store » possède un tout nouveau design."
      },
      {
        "id": 30,
        "question": "Quelle est la date officielle de création de « Wikipédia » en Français ?",
        "propositions": [
          "23 mars 2001",
          "2 janvier 1999",
          "15 janvier 2002",
          "8 décembre 2000"
        ],
        "réponse": "23 mars 2001",
        "anecdote": "Plusieurs moyens de consulter l'encyclopédie existent, tels que des sites web miroirs ou des applications pour smartphone."
      }
    ]
    },
    "en": {
      "débutant": [
      {
        "id": 1,
        "question": "What word processing software has been developed by Microsoft ?",
        "propositions": [
          "Access",
          "PowerPoint",
          "Word",
          "Excel"
        ],
        "réponse": "Word",
        "anecdote": "Microsoft has released several word processing software in the past, but « Word » is still the star."
      },
      {
        "id": 2,
        "question": "The « Excel » software, taken from the Microsoft Office office suite, is a...",
        "propositions": [
          "Internet browser",
          "Spreadsheet",
          "Messaging",
          "Word processing"
        ],
        "réponse": "Spreadsheet",
        "anecdote": "Excel has been criticized several times for its precision problems with floating point calculations."
      },
      {
        "id": 3,
        "question": "In computer science, what is a programming error that has not yet been located ?",
        "propositions": [
          "Crack",
          "Bug",
          "Virus",
          "Spam"
        ],
        "réponse": "Bug",
        "anecdote": "The severity of a computer dysfunction can range from mild to major."
      },
      {
        "id": 4,
        "question": "What version of Windows did Microsoft release on Friday, October 26, 2012 ?",
        "propositions": [
          "Windows 8",
          "Windows Mobile",
          "Windows 7",
          "Windows CE"
        ],
        "réponse": "Windows 8",
        "anecdote": "The Windows 8.1 version is a free update to Windows 8, available since 2013."
      },
      {
        "id": 5,
        "question": "How is desktop publishing commonly abbreviated ?",
        "propositions": [
          "USB",
          "VGA",
          "PAO",
          "CIO"
        ],
        "réponse": "PAO",
        "anecdote": "DTP consists of creating printed documents by working on the composition and typography of documents."
      },
      {
        "id": 6,
        "question": "Which computer application from the Apple company can easily manage an iPod ?",
        "propositions": [
          "QuickTime",
          "FileMaker",
          "iTunes",
          "HyperCard"
        ],
        "réponse": "iTunes",
        "anecdote": "« iTunes » was part of Apple's « iLife » software suite until version '06."
      },
      {
        "id": 7,
        "question": "In computer science, what software can be used to create automatic calculations ?",
        "propositions": [
          "Explorer",
          "Browser",
          "Debugger",
          "Spreadsheet"
        ],
        "réponse": "Spreadsheet",
        "anecdote": "A spreadsheet is a table of information, mostly financial."
      },
      {
        "id": 8,
        "question": "Which hacker breaks protected computer systems and software ?",
        "propositions": [
          "Joker",
          "Pirator",
          "Hacker",
          "Force"
        ],
        "réponse": "Hacker",
        "anecdote": "Some use this know-how within a legal framework, others being more often outlaw."
      },
      {
        "id": 9,
        "question": "What software is used to surf the Internet, on a PC, tablet or smartphone ?",
        "propositions": [
          "Editors",
          "Spreadsheets",
          "Emulators",
          "Browsers"
        ],
        "réponse": "Browsers",
        "anecdote": "The first stable and widely distributed browser was « NCSA Mosaic », in 1993."
      },
      {
        "id": 10,
        "question": "What tool developed by the giant Google allows you to manage your schedule ?",
        "propositions": [
          "Google Mobile",
          "Google Tempo",
          "Google Calendar",
          "Google TimeLine"
        ],
        "réponse": "Google Calendar",
        "anecdote": "« Google Calendar » allows you to share events and calendars and publish them on the internet or on a website."
      }
    ],
    "confirmé": [
      {
        "id": 11,
        "question": "Which large company received the green light in 2011 to buy « Skype » ?",
        "propositions": [
          "Facebook",
          "Google",
          "Microsoft",
          "Apple"
        ],
        "réponse": "Microsoft",
        "anecdote": "« Skype » is free software that allows you to make phone and video calls over the Internet, as well as screen sharing."
      },
      {
        "id": 12,
        "question": "What is probably the best known of the so-called free computer systems ?",
        "propositions": [
          "Windows",
          "MS-DOS",
          "Linux",
          "Mac OS"
        ],
        "réponse": "Linux",
        "anecdote": "Linux is a computer system that runs on hardware ranging from cell phones to supercomputers."
      },
      {
        "id": 13,
        "question": "What is the name of the professional Google services solution ?",
        "propositions": [
          "Google Mac",
          "Google Pro",
          "Google Serve",
          "Google Apps"
        ],
        "réponse": "Google Apps",
        "anecdote": "This website for businesses has many applications online."
      },
      {
        "id": 14,
        "question": "What type of software is made freely and freely available by its creator ?",
        "propositions": [
          "Adware",
          "Software",
          "Malware",
          "Freeware"
        ],
        "réponse": "Freeware",
        "anecdote": "However, one should not confuse freeware (freeware) and shareware (shareware)."
      },
      {
        "id": 15,
        "question": "In April 2012, which start-up Facebook bought for more than a billion dollars ?",
        "propositions": [
          "Globalnet",
          "Backelite",
          "Instagram",
          "Valve"
        ],
        "réponse": "Instagram",
        "anecdote": "« Instagram » is an application co-founded and launched by the American Kevin Systrom and the Brazilian Michel Mike Krieger in October 2010."
      },
      {
        "id": 16,
        "question": "In Quebec, what word is often used to refer to electronic mail ?",
        "propositions": [
          "Email",
          "Lettrinter",
          "Copitel",
          "Emel"
        ],
        "réponse": "Email",
        "anecdote": "Email tends to be recognized as a valid way to contact someone."
      },
      {
        "id": 17,
        "question": "Which software bought by Microsoft replaced « Windows Live Messenger » in 2013 ?",
        "propositions": [
          "Skype",
          "Pidgin",
          "QuickTime",
          "Instagram"
        ],
        "réponse": "Skype",
        "anecdote": "« Skype » was founded in Estonia by Niklas Zennström and Janus Friis in 2003 and developed by three Estonians behind the software « KaZaA »."
      },
      {
        "id": 18,
        "question": "What was the name of the previous Internet browser that became « Microsoft Edge » ?",
        "propositions": [
          "Safari",
          "Chrome",
          "Internet Explorer",
          "Firefox"
        ],
        "réponse": "Internet Explorer",
        "anecdote": "Version 11 of the « Internet Explorer » browser will still be present in Windows 10 before the gradual transition to « Microsoft Edge »."
      },
      {
        "id": 19,
        "question": "What software is essential to protect your computer on the Internet ?",
        "propositions": [
          "Messaging",
          "Cat",
          "Antivirus",
          "Browser"
        ],
        "réponse": "Antivirus",
        "anecdote": "Antivirus programs can scan the contents of a hard drive as well as computer RAM."
      },
      {
        "id": 20,
        "question": "Who is the very first pope to post on « Twitter » ?",
        "propositions": [
          "Benedict XVI",
          "Paul VI",
          "John Paul II",
          "Francois"
        ],
        "réponse": "Benedict XVI",
        "anecdote": "Renowned conservative, Cardinal Ratzinger was elected on April 19, 2005 to succeed John Paul II."
      }
    ],
    "expert": [
      {
        "id": 21,
        "question": "Which e-mail created by Mozilla is the ideal companion for the « Firefox » browser ?",
        "propositions": [
          "Foxmail",
          "Thunderbird",
          "Incredimail",
          "Sylpheed"
        ],
        "réponse": "Thunderbird",
        "anecdote": "Just like « Firefox », « Thunderbird » and its XUL interface is based on the Gecko engine."
      },
      {
        "id": 22,
        "question": "What is the name of the online office suite offered by Microsoft ?",
        "propositions": [
          "KOffice",
          "Office 365",
          "OpenOffice",
          "StarOffice"
        ],
        "réponse": "Office 365",
        "anecdote": "« Office 365 » subscriptions for individuals allow you to benefit from the full version of the Office suite that we know."
      },
      {
        "id": 23,
        "question": "What was the code name for Microsoft Windows version 3.1 ?",
        "propositions": [
          "Janus",
          "Opus",
          "Startus",
          "Uranus"
        ],
        "réponse": "Janus",
        "anecdote": "Version 3 was the first to achieve widespread success, allowing Microsoft to compete with the Apple Macintosh."
      },
      {
        "id": 24,
        "question": "What is the name of Windows Live's online storage service ?",
        "propositions": [
          "Dropbox",
          "RapidShare",
          "MediaFire",
          "Onedrive"
        ],
        "réponse": "Onedrive",
        "anecdote": "This online storage and application service, created in 2007, is a manifestation of the concept of cloud computing."
      },
      {
        "id": 25,
        "question": "What is the new name of the free instant messaging software « Gaim » ?",
        "propositions": [
          "iShare",
          "Connect",
          "Pidgin",
          "Komunnity"
        ],
        "réponse": "Pidgin",
        "anecdote": "« Gaim » was renamed « Pidgin » in 2007 because of complaints from AOL and its AIM brand."
      },
      {
        "id": 26,
        "question": "Which software suite is equivalent to Microsoft Office at the giant Google ?",
        "propositions": [
          "Works",
          "OpenOffice",
          "Google Sites",
          "Google Documents"
        ],
        "réponse": "Google Documents",
        "anecdote": "« Google Documents » is a continuation of the evolutions of « Google Spreadsheets » and « Writely », word processing software."
      },
      {
        "id": 27,
        "question": "What country is the free « Opera » software suite from ?",
        "propositions": [
          "France",
          "Norway",
          "Italy",
          "Austria"
        ],
        "réponse": "Norway",
        "anecdote": "« Opera » is a web browser developed by the Norwegian company Opera Software, which offers several Internet related software."
      },
      {
        "id": 28,
        "question": "Which of these tools does not allow you to view web pages ?",
        "propositions": [
          "Mozilla Firefox",
          "Google Chrome",
          "Acrobat Reader",
          "Internet Explorer"
        ],
        "réponse": "Acrobat Reader",
        "anecdote": "Adobe regularly changes the name of the products of the Acrobat family and this by subdividing its range."
      },
      {
        "id": 29,
        "question": "How many downloads were there on the famous « App Store » at the end of 2012 ?",
        "propositions": [
          "25 billion",
          "35 billion",
          "15 billion",
          "5 billion"
        ],
        "réponse": "35 billion",
        "anecdote": "Since the update of the Apple iOS 7 operating system in September 2013, the « App Store » has a completely new design."
      },
      {
        "id": 30,
        "question": "What is the official date of creation of « Wikipedia » in French ?",
        "propositions": [
          "March 23, 2001",
          "December 8, 2000",
          "January 15, 2002",
          "January 2, 1999"
        ],
        "réponse": "March 23, 2001",
        "anecdote": "There are several ways to consult the encyclopedia, such as mirror websites or smartphone applications."
      }
    ]
    },
    "de": {
      "débutant": [
      {
        "id": 1,
        "question": "Welche Textverarbeitungssoftware wurde von Microsoft entwickelt ?",
        "propositions": [
          "PowerPoint",
          "Wort",
          "Zugriff",
          "Excel"
        ],
        "réponse": "Wort",
        "anecdote": "Microsoft hat in der Vergangenheit mehrere Textverarbeitungsprogramme veröffentlicht, aber « Word » ist immer noch der Star."
      },
      {
        "id": 2,
        "question": "Die Software « Excel » aus der Microsoft Office Office Suite ist eine...",
        "propositions": [
          "Internetbrowser",
          "Textverarbeitung",
          "Tabellenkalkulation",
          "Messaging"
        ],
        "réponse": "Tabellenkalkulation",
        "anecdote": "Excel wurde mehrfach wegen seiner Präzisionsprobleme bei Gleitkommaberechnungen kritisiert."
      },
      {
        "id": 3,
        "question": "Was ist in der Informatik ein Programmierfehler, der noch nicht gefunden wurde ?",
        "propositions": [
          "Virus",
          "Riss",
          "Spam",
          "Bug"
        ],
        "réponse": "Bug",
        "anecdote": "Der Schweregrad einer Computerfunktionsstörung kann von leicht bis schwer reichen."
      },
      {
        "id": 4,
        "question": "Welche Windows-Version hat Microsoft am Freitag, 26. Oktober 2012, veröffentlicht ?",
        "propositions": [
          "Windows 8",
          "Windows 7",
          "Windows Mobile",
          "Windows CE"
        ],
        "réponse": "Windows 8",
        "anecdote": "Die Windows 8.1-Version ist ein kostenloses Update für Windows 8, das seit 2013 verfügbar ist."
      },
      {
        "id": 5,
        "question": "Wie wird Desktop Publishing allgemein abgekürzt ?",
        "propositions": [
          "USB",
          "VGA",
          "PAO",
          "CIO"
        ],
        "réponse": "PAO",
        "anecdote": "DTP besteht aus der Erstellung gedruckter Dokumente, indem an der Zusammensetzung und Typografie von Dokumenten gearbeitet wird."
      },
      {
        "id": 6,
        "question": "Welche Computeranwendung der Firma Apple kann einen iPod problemlos verwalten ?",
        "propositions": [
          "FileMaker",
          "HyperCard",
          "iTunes",
          "QuickTime"
        ],
        "réponse": "iTunes",
        "anecdote": "« iTunes » war bis zur Version '06 Teil der « iLife » -Software-Suite von Apple."
      },
      {
        "id": 7,
        "question": "Mit welcher Software können in der Informatik automatische Berechnungen erstellt werden ?",
        "propositions": [
          "Tabellenkalkulation",
          "Explorer",
          "Debugger",
          "Browser"
        ],
        "réponse": "Tabellenkalkulation",
        "anecdote": "Eine Tabelle ist eine Tabelle mit Informationen, hauptsächlich finanzielle."
      },
      {
        "id": 8,
        "question": "Welcher Hacker bricht geschützte Computersysteme und Software ?",
        "propositions": [
          "Pirator",
          "Kraft",
          "Hacker",
          "Joker"
        ],
        "réponse": "Hacker",
        "anecdote": "Einige nutzen dieses Know-how innerhalb eines rechtlichen Rahmens, andere sind häufiger gesetzwidrig."
      },
      {
        "id": 9,
        "question": "Mit welcher Software können Sie auf einem PC, Tablet oder Smartphone im Internet surfen ?",
        "propositions": [
          "Redaktion",
          "Browser",
          "Tabellenkalkulation",
          "Emulatoren"
        ],
        "réponse": "Browser",
        "anecdote": "Der erste stabile und weit verbreitete Browser war 1993 « NCSA Mosaic »."
      },
      {
        "id": 10,
        "question": "Mit welchem vom Riesen Google entwickelten Tool können Sie Ihren Zeitplan verwalten ?",
        "propositions": [
          "Google Mobile",
          "Google TimeLine",
          "Google Tempo",
          "Google Kalender"
        ],
        "réponse": "Google Kalender",
        "anecdote": "Mit « Google Kalender » können Sie Ereignisse und Kalender freigeben und im Internet oder auf einer Website veröffentlichen."
      }
    ],
    "confirmé": [
      {
        "id": 11,
        "question": "Welches große Unternehmen erhielt 2011 grünes Licht für den Kauf von « Skype » ?",
        "propositions": [
          "Facebook",
          "Apple",
          "Microsoft",
          "Google"
        ],
        "réponse": "Microsoft",
        "anecdote": "« Skype » ist eine kostenlose Software, mit der Sie Telefon- und Videoanrufe über das Internet sowie Bildschirmfreigaben tätigen können."
      },
      {
        "id": 12,
        "question": "Was ist wohl das bekannteste der sogenannten freien Computersysteme ?",
        "propositions": [
          "Mac OS",
          "Linux",
          "Windows",
          "MS-DOS"
        ],
        "réponse": "Linux",
        "anecdote": "Linux ist ein Computersystem, das auf Hardware läuft, die von Mobiltelefonen bis zu Supercomputern reicht."
      },
      {
        "id": 13,
        "question": "Wie heißt die professionelle Google Services-Lösung ?",
        "propositions": [
          "Google Serve",
          "Google Mac",
          "Google Pro",
          "Google Apps"
        ],
        "réponse": "Google Apps",
        "anecdote": "Diese Website für Unternehmen hat viele Anwendungen online."
      },
      {
        "id": 14,
        "question": "Welche Art von Software wird vom Ersteller frei und frei verfügbar gemacht ?",
        "propositions": [
          "Software",
          "Freeware",
          "Adware",
          "Malware"
        ],
        "réponse": "Freeware",
        "anecdote": "Man sollte jedoch Freeware (Freeware) und Shareware (Shareware) nicht verwechseln."
      },
      {
        "id": 15,
        "question": "Welches Start-up hat Facebook im April 2012 für mehr als eine Milliarde Dollar gekauft ?",
        "propositions": [
          "Backelite",
          "Ventil",
          "Instagram",
          "Globalnet"
        ],
        "réponse": "Instagram",
        "anecdote": "« Instagram » ist eine Anwendung, die im Oktober 2010 vom Amerikaner Kevin Systrom und dem Brasilianer Michel Mike Krieger mitbegründet und gestartet wurde."
      },
      {
        "id": 16,
        "question": "Welches Wort wird in Quebec häufig für E-Mail verwendet ?",
        "propositions": [
          "Lettrinter",
          "Emel",
          "E-Mail",
          "Copitel"
        ],
        "réponse": "E-Mail",
        "anecdote": "E-Mails werden in der Regel als gültige Möglichkeit zur Kontaktaufnahme erkannt."
      },
      {
        "id": 17,
        "question": "Welche von Microsoft gekaufte Software hat 2013 « Windows Live Messenger » ersetzt ?",
        "propositions": [
          "Skype",
          "Pidgin",
          "Instagram",
          "QuickTime"
        ],
        "réponse": "Skype",
        "anecdote": "« Skype » wurde 2003 in Estland von Niklas Zennström und Janus Friis gegründet und von drei Esten hinter der Software « KaZaA » entwickelt."
      },
      {
        "id": 18,
        "question": "Wie hieß der vorherige Internetbrowser, der zu « Microsoft Edge » wurde ?",
        "propositions": [
          "Firefox",
          "Chrome",
          "Internet Explorer",
          "Safari"
        ],
        "réponse": "Internet Explorer",
        "anecdote": "Version 11 des Browsers « Internet Explorer » ist vor dem schrittweisen Übergang zu « Microsoft Edge » weiterhin in Windows 10 vorhanden."
      },
      {
        "id": 19,
        "question": "Welche Software ist wichtig, um Ihren Computer im Internet zu schützen ?",
        "propositions": [
          "Browser",
          "Katze",
          "Messaging",
          "Antivirus"
        ],
        "réponse": "Antivirus",
        "anecdote": "Antivirenprogramme können den Inhalt einer Festplatte sowie den Computer-RAM scannen."
      },
      {
        "id": 20,
        "question": "Wer ist der erste Papst, der auf « Twitter » schreibt ?",
        "propositions": [
          "Benedikt XVI",
          "Francois",
          "Paul VI",
          "Johannes Paul II."
        ],
        "réponse": "Benedikt XVI",
        "anecdote": "Der bekannte Konservative Kardinal Ratzinger wurde am 19. April 2005 als Nachfolger von Johannes Paul II. Gewählt."
      }
    ],
    "expert": [
      {
        "id": 21,
        "question": "Welche von Mozilla erstellte E-Mail ist der ideale Begleiter für den Browser « Firefox » ?",
        "propositions": [
          "Foxmail",
          "Sylpheed",
          "Incredimail",
          "Thunderbird"
        ],
        "réponse": "Thunderbird",
        "anecdote": "Genau wie « Firefox » basiert « Thunderbird » und seine XUL-Schnittstelle auf der Gecko-Engine."
      },
      {
        "id": 22,
        "question": "Wie heißt die von Microsoft angebotene Online-Office-Suite ?",
        "propositions": [
          "Office 365",
          "KOffice",
          "OpenOffice",
          "StarOffice"
        ],
        "réponse": "Office 365",
        "anecdote": "Mit « Office 365 » -Abonnements für Einzelpersonen können Sie von der uns bekannten Vollversion der Office-Suite profitieren."
      },
      {
        "id": 23,
        "question": "Wie lautete der Codename für Microsoft Windows Version 3.1 ?",
        "propositions": [
          "Janus",
          "Startus",
          "Uranus",
          "Opus"
        ],
        "réponse": "Janus",
        "anecdote": "Version 3 war die erste, die weit verbreitete Erfolge erzielte und es Microsoft ermöglichte, mit dem Apple Macintosh zu konkurrieren."
      },
      {
        "id": 24,
        "question": "Wie heißt der Online-Speicherdienst von Windows Live ?",
        "propositions": [
          "RapidShare",
          "Dropbox",
          "Onedrive",
          "MediaFire"
        ],
        "réponse": "Onedrive",
        "anecdote": "Dieser 2007 erstellte Online-Speicher- und Anwendungsdienst ist Ausdruck des Konzepts des Cloud Computing."
      },
      {
        "id": 25,
        "question": "Wie lautet der neue Name der kostenlosen Instant-Messaging-Software « Gaim » ?",
        "propositions": [
          "Komunnity",
          "iShare",
          "Connect",
          "Pidgin"
        ],
        "réponse": "Pidgin",
        "anecdote": "« Gaim » wurde 2007 aufgrund von Beschwerden von AOL und seiner Marke AIM in « Pidgin » umbenannt."
      },
      {
        "id": 26,
        "question": "Welche Software-Suite entspricht Microsoft Office beim Riesen Google ?",
        "propositions": [
          "OpenOffice",
          "Google Dokumente",
          "Google Sites",
          "Funktioniert"
        ],
        "réponse": "Google Dokumente",
        "anecdote": "« Google Dokumente » ist eine Fortsetzung der Weiterentwicklung der Textverarbeitungssoftware « Google Spreadsheets » und « Writely »."
      },
      {
        "id": 27,
        "question": "Aus welchem Land stammt die kostenlose « Opera » Software-Suite ?",
        "propositions": [
          "Italien",
          "Frankreich",
          "Norwegen",
          "Österreich"
        ],
        "réponse": "Norwegen",
        "anecdote": "« Opera » ist ein Webbrowser, der von der norwegischen Firma Opera Software entwickelt wurde und verschiedene internetbezogene Software anbietet."
      },
      {
        "id": 28,
        "question": "Mit welchem dieser Tools können Sie keine Webseiten anzeigen ?",
        "propositions": [
          "Acrobat Reader",
          "Internet Explorer",
          "Google Chrome",
          "Mozilla Firefox"
        ],
        "réponse": "Acrobat Reader",
        "anecdote": "Adobe ändert regelmäßig den Namen der Produkte der Acrobat-Familie, indem das Sortiment unterteilt wird."
      },
      {
        "id": 29,
        "question": "Wie viele Downloads gab es Ende 2012 im berühmten « App Store » ?",
        "propositions": [
          "5 Milliarden",
          "15 Milliarden",
          "25 Milliarden",
          "35 Milliarden"
        ],
        "réponse": "35 Milliarden",
        "anecdote": "Seit dem Update des Betriebssystems von Apple iOS 7 im September 2013 hat der « App Store » ein völlig neues Design."
      },
      {
        "id": 30,
        "question": "Was ist das offizielle Erstellungsdatum von « Wikipedia » auf Französisch ?",
        "propositions": [
          "23. März 2001",
          "2. Januar 1999",
          "8. Dezember 2000",
          "15. Januar 2002"
        ],
        "réponse": "23. März 2001",
        "anecdote": "Es gibt verschiedene Möglichkeiten, die Enzyklopädie zu konsultieren, z."
      }
    ]
    },
    "es": {
      "débutant": [
      {
        "id": 1,
        "question": "¿Qué software de procesamiento de textos ha desarrollado Microsoft ?",
        "propositions": [
          "Excel",
          "Palabra",
          "Acceso",
          "PowerPoint"
        ],
        "réponse": "Palabra",
        "anecdote": "Microsoft ha lanzado varios programas de procesamiento de texto en el pasado, pero « Word » sigue siendo la estrella."
      },
      {
        "id": 2,
        "question": "El software « Excel », tomado de la suite ofimática de Microsoft Office, es un...",
        "propositions": [
          "Procesamiento de textos",
          "Excel ha sido criticado varias veces por",
          "Mensajería",
          "Navegador de internet"
        ],
        "réponse": "Procesamiento de textos",
        "anecdote": ""
      },
      {
        "id": 3,
        "question": "En informática, ¿qué es un error de programación que aún no se ha localizado ?",
        "propositions": [
          "Spam",
          "Crack",
          "Virus",
          "Bug"
        ],
        "réponse": "Bug",
        "anecdote": "La gravedad de una disfunción informática puede variar de leve a grave."
      },
      {
        "id": 4,
        "question": "¿Qué versión de Windows lanzó Microsoft el viernes 26 de octubre de 2012 ?",
        "propositions": [
          "Windows 8",
          "Windows Mobile",
          "Windows CE",
          "Windows 7"
        ],
        "réponse": "Windows 8",
        "anecdote": "La versión de Windows 8.1 es una actualización gratuita de Windows 8, disponible desde 2013."
      },
      {
        "id": 5,
        "question": "¿Cómo se abrevia comúnmente la autoedición ?",
        "propositions": [
          "CIO",
          "PAO",
          "VGA",
          "USB"
        ],
        "réponse": "PAO",
        "anecdote": "DTP consiste en crear documentos impresos trabajando en la composición y tipografía de los documentos."
      },
      {
        "id": 6,
        "question": "¿Qué aplicación informática de la empresa Apple puede administrar fácilmente un iPod ?",
        "propositions": [
          "HyperCard",
          "FileMaker",
          "QuickTime",
          "iTunes"
        ],
        "réponse": "iTunes",
        "anecdote": "« iTunes » formaba parte del paquete de software « iLife » de Apple hasta la versión '06."
      },
      {
        "id": 7,
        "question": "En informática, ¿qué software se puede utilizar para crear cálculos automáticos ?",
        "propositions": [
          "Depurador",
          "Hoja de cálculo",
          "Explorer",
          "Navegador"
        ],
        "réponse": "Hoja de cálculo",
        "anecdote": "Una hoja de cálculo es una tabla de información, principalmente financiera."
      },
      {
        "id": 8,
        "question": "¿Qué hacker rompe el software y los sistemas informáticos protegidos ?",
        "propositions": [
          "Pirator",
          "Joker",
          "Fuerza",
          "Hacker"
        ],
        "réponse": "Hacker",
        "anecdote": "Algunos utilizan este conocimiento dentro de un marco legal, mientras que otros son más a menudo ilegales."
      },
      {
        "id": 9,
        "question": "¿Qué software se utiliza para navegar por Internet, en una PC, tableta o teléfono inteligente ?",
        "propositions": [
          "Hojas de cálculo",
          "Editores",
          "Emuladores",
          "Navegadores"
        ],
        "réponse": "Navegadores",
        "anecdote": "El primer navegador estable y ampliamente distribuido fue « NCSA Mosaic », en 1993."
      },
      {
        "id": 10,
        "question": "¿Qué herramienta desarrollada por el gigante Google te permite gestionar tu agenda ?",
        "propositions": [
          "Google Tempo",
          "Google para móviles",
          "Calendario de Google",
          "Google TimeLine"
        ],
        "réponse": "Calendario de Google",
        "anecdote": "« Google Calendar » le permite compartir eventos y calendarios y publicarlos en Internet o en un sitio web."
      }
    ],
    "confirmé": [
      {
        "id": 11,
        "question": "¿Qué gran empresa recibió luz verde en 2011 para comprar « Skype » ?",
        "propositions": [
          "Google",
          "Apple",
          "Facebook",
          "Microsoft"
        ],
        "réponse": "Microsoft",
        "anecdote": "« Skype » es un software gratuito que le permite realizar llamadas telefónicas y videollamadas a través de Internet, así como compartir pantalla."
      },
      {
        "id": 12,
        "question": "¿Cuál es probablemente el más conocido de los llamados sistemas informáticos libres ?",
        "propositions": [
          "Linux",
          "Windows",
          "Mac OS",
          "MS-DOS"
        ],
        "réponse": "Linux",
        "anecdote": "Linux es un sistema informático que se ejecuta en hardware que va desde teléfonos móviles hasta supercomputadoras."
      },
      {
        "id": 13,
        "question": "¿Cuál es el nombre de la solución de servicios profesionales de Google ?",
        "propositions": [
          "Google Mac",
          "Google Apps",
          "Google Pro",
          "Servicio de Google"
        ],
        "réponse": "Google Apps",
        "anecdote": "Este sitio web para empresas tiene muchas aplicaciones en línea."
      },
      {
        "id": 14,
        "question": "¿Qué tipo de software pone a disposición libre y gratuita su creador ?",
        "propositions": [
          "Software",
          "Freeware",
          "Adware",
          "Software malicioso"
        ],
        "réponse": "Freeware",
        "anecdote": "Sin embargo, no se debe confundir freeware (freeware) y shareware (shareware)."
      },
      {
        "id": 15,
        "question": "En abril de 2012, ¿qué startup compró Facebook por más de mil millones de dólares ?",
        "propositions": [
          "Backelite",
          "Instagram",
          "Globalnet",
          "Válvula"
        ],
        "réponse": "Instagram",
        "anecdote": "« Instagram » es una aplicación cofundada y lanzada por el estadounidense Kevin Systrom y el brasileño Michel Mike Krieger en octubre de 2010."
      },
      {
        "id": 16,
        "question": "En Quebec, ¿qué palabra se usa a menudo para referirse al correo electrónico ?",
        "propositions": [
          "Emel",
          "Copitel",
          "Correo electrónico",
          "Lettrinter"
        ],
        "réponse": "Correo electrónico",
        "anecdote": "El correo electrónico tiende a ser reconocido como una forma válida de contactar a alguien."
      },
      {
        "id": 17,
        "question": "¿Qué software comprado por Microsoft reemplazó a « Windows Live Messenger » en 2013 ?",
        "propositions": [
          "Pidgin",
          "Skype",
          "QuickTime",
          "Instagram"
        ],
        "réponse": "Skype",
        "anecdote": "« Skype » fue fundado en Estonia por Niklas Zennström y Janus Friis en 2003 y desarrollado por tres estonios detrás del software « KaZaA »."
      },
      {
        "id": 18,
        "question": "¿Cuál era el nombre del navegador de Internet anterior que se convirtió en « Microsoft Edge » ?",
        "propositions": [
          "Firefox",
          "Safari",
          "Internet Explorer",
          "Chrome"
        ],
        "réponse": "Internet Explorer",
        "anecdote": "La versión 11 del navegador « Internet Explorer » seguirá estando presente en Windows 10 antes de la transición gradual a « Microsoft Edge »."
      },
      {
        "id": 19,
        "question": "¿Qué software es esencial para proteger su computadora en Internet ?",
        "propositions": [
          "Navegador",
          "Antivirus",
          "Gato",
          "Mensajería"
        ],
        "réponse": "Antivirus",
        "anecdote": "Los programas antivirus pueden escanear el contenido de un disco duro y la RAM de la computadora."
      },
      {
        "id": 20,
        "question": "¿Quién es el primer Papa en publicar en « Twitter » ?",
        "propositions": [
          "Paul VI",
          "Benedicto XVI",
          "Francois",
          "Juan Pablo II"
        ],
        "réponse": "Benedicto XVI",
        "anecdote": "Conservador de renombre, el cardenal Ratzinger fue elegido el 19 de abril de 2005 para suceder a Juan Pablo II."
      }
    ],
    "expert": [
      {
        "id": 21,
        "question": "¿Qué correo electrónico creado por Mozilla es el compañero ideal para el navegador « Firefox » ?",
        "propositions": [
          "Thunderbird",
          "Foxmail",
          "Sylpheed",
          "Increíble"
        ],
        "réponse": "Thunderbird",
        "anecdote": "Al igual que « Firefox », « Thunderbird » y su interfaz XUL se basa en el motor Gecko."
      },
      {
        "id": 22,
        "question": "¿Cómo se llama la suite ofimática en línea que ofrece Microsoft ?",
        "propositions": [
          "StarOffice",
          "Office 365",
          "OpenOffice",
          "KOffice"
        ],
        "réponse": "Office 365",
        "anecdote": "Las suscripciones a « Office 365 » para particulares le permiten beneficiarse de la versión completa del paquete de Office que conocemos."
      },
      {
        "id": 23,
        "question": "¿Cuál era el nombre en clave de la versión 3.1 de Microsoft Windows ?",
        "propositions": [
          "Janus",
          "Opus",
          "Urano",
          "Startus"
        ],
        "réponse": "Janus",
        "anecdote": "La versión 3 fue la primera en lograr un éxito generalizado, lo que permitió a Microsoft competir con Apple Macintosh."
      },
      {
        "id": 24,
        "question": "¿Cuál es el nombre del servicio de almacenamiento en línea de Windows Live ?",
        "propositions": [
          "RapidShare",
          "MediaFire",
          "Dropbox",
          "Onedrive"
        ],
        "réponse": "Onedrive",
        "anecdote": "Este servicio de aplicaciones y almacenamiento en línea, creado en 2007, es una manifestación del concepto de computación en la nube."
      },
      {
        "id": 25,
        "question": "¿Cuál es el nuevo nombre del software gratuito de mensajería instantánea « Gaim » ?",
        "propositions": [
          "Pidgin",
          "Connect",
          "Komunnity",
          "iShare"
        ],
        "réponse": "Pidgin",
        "anecdote": "« Gaim » cambió su nombre a « Pidgin » en 2007 debido a quejas de AOL y su marca AIM."
      },
      {
        "id": 26,
        "question": "¿Qué paquete de software es equivalente a Microsoft Office en el gigante Google ?",
        "propositions": [
          "Funciona",
          "OpenOffice",
          "Google Sites",
          "Documentos de Google"
        ],
        "réponse": "Documentos de Google",
        "anecdote": "« Google Documents » es una continuación de las evoluciones de « Google Spreadsheets » y « Writely », software de procesamiento de texto."
      },
      {
        "id": 27,
        "question": "¿De qué país es el paquete de software gratuito « Opera » ?",
        "propositions": [
          "Austria",
          "Italia",
          "Francia",
          "Noruega"
        ],
        "réponse": "Noruega",
        "anecdote": "« Opera » es un navegador web desarrollado por la empresa noruega Opera Software, que ofrece varios programas relacionados con Internet."
      },
      {
        "id": 28,
        "question": "¿Cuál de estas herramientas no le permite ver páginas web ?",
        "propositions": [
          "Internet Explorer",
          "Google Chrome",
          "Acrobat Reader",
          "Mozilla Firefox"
        ],
        "réponse": "Acrobat Reader",
        "anecdote": "Adobe cambia regularmente el nombre de los productos de la familia Acrobat y esto subdividiendo su gama."
      },
      {
        "id": 29,
        "question": "¿Cuántas descargas hubo en la famosa « App Store » a finales de 2012 ?",
        "propositions": [
          "35 mil millones",
          "25 mil millones",
          "5 mil millones",
          "15 mil millones"
        ],
        "réponse": "35 mil millones",
        "anecdote": "Desde la actualización del sistema operativo de Apple iOS 7 en septiembre de 2013, la « App Store » tiene un diseño completamente nuevo."
      },
      {
        "id": 30,
        "question": "¿Cuál es la fecha oficial de creación de « Wikipedia » en francés ?",
        "propositions": [
          "8 de diciembre de 2000",
          "23 de marzo de 2001",
          "2 de enero de 1999",
          "15 de enero de 2002"
        ],
        "réponse": "23 de marzo de 2001",
        "anecdote": "Hay varias formas de consultar la enciclopedia, como sitios web espejo o aplicaciones para teléfonos inteligentes."
      }
    ]
    },
    "it": {
      "débutant": [
      {
        "id": 1,
        "question": "Quale software di elaborazione testi è stato sviluppato da Microsoft ?",
        "propositions": [
          "Excel",
          "Accesso",
          "Word",
          "PowerPoint"
        ],
        "réponse": "Word",
        "anecdote": "Microsoft ha rilasciato diversi software di elaborazione testi in passato, ma « Word » è ancora il protagonista."
      },
      {
        "id": 2,
        "question": "Il software « Excel », tratto dalla suite per ufficio Microsoft Office, è un...",
        "propositions": [
          "Messaggistica",
          "Foglio di calcolo",
          "Browser Internet",
          "Elaborazione di testi"
        ],
        "réponse": "Foglio di calcolo",
        "anecdote": "Excel è stato criticato più volte per i suoi problemi di precisione con i calcoli in virgola mobile."
      },
      {
        "id": 3,
        "question": "In informatica, cos'è un errore di programmazione che non è stato ancora individuato ?",
        "propositions": [
          "Spam",
          "Bug",
          "Crack",
          "Virus"
        ],
        "réponse": "Bug",
        "anecdote": "La gravità di una disfunzione del computer può variare da lieve a grave."
      },
      {
        "id": 4,
        "question": "Quale versione di Windows ha rilasciato Microsoft venerdì 26 ottobre 2012 ?",
        "propositions": [
          "Windows 7",
          "Windows 8",
          "Windows Mobile",
          "Windows CE"
        ],
        "réponse": "Windows 8",
        "anecdote": "La versione per Windows 8.1 è un aggiornamento gratuito di Windows 8, disponibile dal 2013."
      },
      {
        "id": 5,
        "question": "Come viene comunemente abbreviato il desktop publishing ?",
        "propositions": [
          "USB",
          "CIO",
          "PAO",
          "VGA"
        ],
        "réponse": "PAO",
        "anecdote": "DTP consiste nel creare documenti stampati lavorando sulla composizione e la tipografia dei documenti."
      },
      {
        "id": 6,
        "question": "Quale applicazione per computer dell'azienda Apple può gestire facilmente un iPod ?",
        "propositions": [
          "iTunes",
          "QuickTime",
          "HyperCard",
          "FileMaker"
        ],
        "réponse": "iTunes",
        "anecdote": "« iTunes » faceva parte della suite di software « iLife » di Apple fino alla versione '06."
      },
      {
        "id": 7,
        "question": "In informatica, quale software può essere utilizzato per creare calcoli automatici ?",
        "propositions": [
          "Debugger",
          "Foglio di calcolo",
          "Explorer",
          "Browser"
        ],
        "réponse": "Foglio di calcolo",
        "anecdote": "Un foglio di calcolo è una tabella di informazioni, principalmente finanziarie."
      },
      {
        "id": 8,
        "question": "Quale hacker rompe sistemi informatici e software protetti ?",
        "propositions": [
          "Forza",
          "Joker",
          "Pirator",
          "Hacker"
        ],
        "réponse": "Hacker",
        "anecdote": "Alcuni utilizzano questo know-how all'interno di un quadro giuridico, altri sono più spesso fuorilegge."
      },
      {
        "id": 9,
        "question": "Quale software viene utilizzato per navigare in Internet, su PC, tablet o smartphone ?",
        "propositions": [
          "Editori",
          "Emulatori",
          "Browser",
          "Fogli di lavoro"
        ],
        "réponse": "Browser",
        "anecdote": "Il primo browser stabile e ampiamente distribuito è stato « NCSA Mosaic », nel 1993."
      },
      {
        "id": 10,
        "question": "Quale strumento sviluppato dal colosso Google ti permette di gestire i tuoi impegni ?",
        "propositions": [
          "Google Calendar",
          "Google Tempo",
          "Google Mobile",
          "Google TimeLine"
        ],
        "réponse": "Google Calendar",
        "anecdote": "« Google Calendar » ti consente di condividere eventi e calendari e di pubblicarli su Internet o su un sito web."
      }
    ],
    "confirmé": [
      {
        "id": 11,
        "question": "Quale grande azienda ha ricevuto il via libera nel 2011 per acquistare « Skype » ?",
        "propositions": [
          "Facebook",
          "Google",
          "Apple",
          "Microsoft"
        ],
        "réponse": "Microsoft",
        "anecdote": "« Skype » è un software gratuito che ti consente di effettuare telefonate e videochiamate su Internet, oltre alla condivisione dello schermo."
      },
      {
        "id": 12,
        "question": "Qual è probabilmente il più noto dei cosiddetti sistemi informatici liberi ?",
        "propositions": [
          "MS-DOS",
          "Linux",
          "Mac OS",
          "Windows"
        ],
        "réponse": "Linux",
        "anecdote": "Linux è un sistema informatico che funziona su hardware che va dai telefoni cellulari ai supercomputer."
      },
      {
        "id": 13,
        "question": "Qual è il nome della soluzione dei servizi professionali di Google ?",
        "propositions": [
          "Google Apps",
          "Google Mac",
          "Google Pro",
          "Google Serve"
        ],
        "réponse": "Google Apps",
        "anecdote": "Questo sito Web per le aziende ha molte applicazioni online."
      },
      {
        "id": 14,
        "question": "Che tipo di software è reso liberamente e liberamente disponibile dal suo creatore ?",
        "propositions": [
          "Adware",
          "Malware",
          "Gratuito",
          "Software"
        ],
        "réponse": "Gratuito",
        "anecdote": "Tuttavia, non si dovrebbe confondere freeware (freeware) e shareware (shareware)."
      },
      {
        "id": 15,
        "question": "Nell'aprile 2012, quale start-up Facebook ha acquistato per più di un miliardo di dollari ?",
        "propositions": [
          "Valvola",
          "Instagram",
          "Backelite",
          "Globalnet"
        ],
        "réponse": "Instagram",
        "anecdote": "« Instagram » è un'applicazione co-fondata e lanciata dall'americano Kevin Systrom e dal brasiliano Michel Mike Krieger nell'ottobre 2010."
      },
      {
        "id": 16,
        "question": "In Quebec, quale parola viene spesso usata per riferirsi alla posta elettronica ?",
        "propositions": [
          "Lettrinter",
          "E-mail",
          "Emel",
          "Copitel"
        ],
        "réponse": "E-mail",
        "anecdote": "L'email tende ad essere riconosciuta come un modo valido per contattare qualcuno."
      },
      {
        "id": 17,
        "question": "Quale software acquistato da Microsoft ha sostituito « Windows Live Messenger » nel 2013 ?",
        "propositions": [
          "Instagram",
          "Pidgin",
          "QuickTime",
          "Skype"
        ],
        "réponse": "Skype",
        "anecdote": "« Skype » è stato fondato in Estonia da Niklas Zennström e Janus Friis nel 2003 e sviluppato da tre estoni dietro il software « KaZaA »."
      },
      {
        "id": 18,
        "question": "Qual era il nome del browser Internet precedente che divenne « Microsoft Edge » ?",
        "propositions": [
          "Chrome",
          "Firefox",
          "Internet Explorer",
          "Safari"
        ],
        "réponse": "Internet Explorer",
        "anecdote": "La versione 11 del browser « Internet Explorer » sarà ancora presente in Windows 10 prima della transizione graduale a « Microsoft Edge »."
      },
      {
        "id": 19,
        "question": "Quale software è essenziale per proteggere il tuo computer su Internet ?",
        "propositions": [
          "Messaggistica",
          "Antivirus",
          "Browser",
          "Gatto"
        ],
        "réponse": "Antivirus",
        "anecdote": "I programmi antivirus possono eseguire la scansione del contenuto di un disco rigido e della RAM del computer."
      },
      {
        "id": 20,
        "question": "Chi è il primo vero papa a postare su « Twitter » ?",
        "propositions": [
          "Paolo VI",
          "Francois",
          "Benedetto XVI",
          "Giovanni Paolo II"
        ],
        "réponse": "Benedetto XVI",
        "anecdote": "Rinomato conservatore, il cardinale Ratzinger è stato eletto il 19 aprile 2005 come successore di Giovanni Paolo II."
      }
    ],
    "expert": [
      {
        "id": 21,
        "question": "Quale e-mail creata da Mozilla è il compagno ideale per il browser « Firefox » ?",
        "propositions": [
          "Incredimail",
          "Foxmail",
          "Thunderbird",
          "Sylpheed"
        ],
        "réponse": "Thunderbird",
        "anecdote": "Proprio come « Firefox », « Thunderbird » e la sua interfaccia XUL è basata sul motore Gecko."
      },
      {
        "id": 22,
        "question": "Qual è il nome della suite per ufficio online offerta da Microsoft ?",
        "propositions": [
          "Office 365",
          "OpenOffice",
          "StarOffice",
          "KOffice"
        ],
        "réponse": "Office 365",
        "anecdote": "Gli abbonamenti a « Office 365 » per utenti privati \u200b\u200bti consentono di beneficiare della versione completa della suite Office che conosciamo."
      },
      {
        "id": 23,
        "question": "Qual era il nome in codice per Microsoft Windows versione 3.1 ?",
        "propositions": [
          "Startus",
          "Janus",
          "Urano",
          "Opus"
        ],
        "réponse": "Janus",
        "anecdote": "La versione 3 è stata la prima a ottenere un successo diffuso, consentendo a Microsoft di competere con l'Apple Macintosh."
      },
      {
        "id": 24,
        "question": "Qual è il nome del servizio di archiviazione online di Windows Live ?",
        "propositions": [
          "Dropbox",
          "MediaFire",
          "Onedrive",
          "RapidShare"
        ],
        "réponse": "Onedrive",
        "anecdote": "Questo servizio di archiviazione e applicazione online, creato nel 2007, è una manifestazione del concetto di cloud computing."
      },
      {
        "id": 25,
        "question": "Qual è il nuovo nome del software gratuito di messaggistica istantanea « Gaim » ?",
        "propositions": [
          "iShare",
          "Connect",
          "Pidgin",
          "Komunnity"
        ],
        "réponse": "Pidgin",
        "anecdote": "« Gaim » è stato rinominato « Pidgin » nel 2007 a causa di reclami di AOL e del suo marchio AIM."
      },
      {
        "id": 26,
        "question": "Quale suite di software è equivalente a Microsoft Office nel gigante di Google ?",
        "propositions": [
          "Google Sites",
          "Funziona",
          "OpenOffice",
          "Documenti Google"
        ],
        "réponse": "Documenti Google",
        "anecdote": "« Google Documents » è una continuazione dell'evoluzione di « Google Spreadsheets » e « Writely », software di elaborazione testi."
      },
      {
        "id": 27,
        "question": "Da quale paese proviene la suite software gratuita « Opera » ?",
        "propositions": [
          "Norvegia",
          "Austria",
          "Italia",
          "Francia"
        ],
        "réponse": "Norvegia",
        "anecdote": "« Opera » è un browser web sviluppato dalla società norvegese Opera Software, che offre diversi software relativi a Internet."
      },
      {
        "id": 28,
        "question": "Quale di questi strumenti non ti consente di visualizzare le pagine web ?",
        "propositions": [
          "Acrobat Reader",
          "Mozilla Firefox",
          "Internet Explorer",
          "Google Chrome"
        ],
        "réponse": "Acrobat Reader",
        "anecdote": "Adobe cambia regolarmente il nome dei prodotti della famiglia Acrobat e questo suddividendone la gamma."
      },
      {
        "id": 29,
        "question": "Quanti download c'erano sul famoso « App Store » alla fine del 2012 ?",
        "propositions": [
          "25 miliardi",
          "5 miliardi",
          "15 miliardi",
          "35 miliardi"
        ],
        "réponse": "35 miliardi",
        "anecdote": "Dall'aggiornamento del sistema operativo di Apple iOS 7 nel settembre 2013, l '« App Store » ha un design completamente nuovo."
      },
      {
        "id": 30,
        "question": "Qual è la data ufficiale di creazione di « Wikipedia » in francese ?",
        "propositions": [
          "2 gennaio 1999",
          "15 gennaio 2002",
          "23 marzo 2001",
          "8 dicembre 2000"
        ],
        "réponse": "23 marzo 2001",
        "anecdote": "Esistono diversi modi per consultare l'enciclopedia, come siti Web mirror o applicazioni per smartphone."
      }
    ]
    },
    "nl": {
      "débutant": [
      {
        "id": 1,
        "question": "Welke tekstverwerkingssoftware is door Microsoft ontwikkeld ?",
        "propositions": [
          "Excel",
          "Toegang",
          "Woord",
          "PowerPoint"
        ],
        "réponse": "Woord",
        "anecdote": "Microsoft heeft in het verleden verschillende tekstverwerkingssoftware uitgebracht, maar « Word » is nog steeds de ster."
      },
      {
        "id": 2,
        "question": "De « Excel » -software, afkomstig uit de Microsoft Office-kantoorsuite, is een...",
        "propositions": [
          "Tekstverwerking",
          "Berichten",
          "Werkblad",
          "Internetbrowser"
        ],
        "réponse": "Werkblad",
        "anecdote": "Excel is meerdere keren bekritiseerd vanwege zijn precisieproblemen met drijvende-kommaberekeningen."
      },
      {
        "id": 3,
        "question": "Wat is in de informatica een programmeerfout die nog niet is gevonden ?",
        "propositions": [
          "Spam",
          "Crack",
          "Virus",
          "Bug"
        ],
        "réponse": "Bug",
        "anecdote": "De ernst van een computerdisfunctie kan variëren van licht tot ernstig."
      },
      {
        "id": 4,
        "question": "Welke versie van Windows heeft Microsoft op vrijdag 26 oktober 2012 uitgebracht ?",
        "propositions": [
          "Windows 7",
          "Windows Mobile",
          "Windows 8",
          "Windows CE"
        ],
        "réponse": "Windows 8",
        "anecdote": "De Windows 8.1-versie is een gratis update naar Windows 8, beschikbaar sinds 2013."
      },
      {
        "id": 5,
        "question": "Hoe wordt desktop publishing gewoonlijk afgekort ?",
        "propositions": [
          "USB",
          "VGA",
          "CIO",
          "PAO"
        ],
        "réponse": "PAO",
        "anecdote": "DTP bestaat uit het maken van gedrukte documenten door te werken aan de samenstelling en typografie van documenten."
      },
      {
        "id": 6,
        "question": "Welke computertoepassing van het Apple-bedrijf kan gemakkelijk een iPod beheren ?",
        "propositions": [
          "HyperCard",
          "FileMaker",
          "QuickTime",
          "iTunes"
        ],
        "réponse": "iTunes",
        "anecdote": "« iTunes » maakte tot versie '06 deel uit van Apple's « iLife » -softwarepakket."
      },
      {
        "id": 7,
        "question": "Welke software kan in de informatica worden gebruikt om automatische berekeningen te maken ?",
        "propositions": [
          "Debugger",
          "Verkenner",
          "Browser",
          "Werkblad"
        ],
        "réponse": "Werkblad",
        "anecdote": "Een spreadsheet is een tabel met informatie, meestal financieel."
      },
      {
        "id": 8,
        "question": "Welke hacker breekt beveiligde computersystemen en software ?",
        "propositions": [
          "Hacker",
          "Force",
          "Pirator",
          "Joker"
        ],
        "réponse": "Hacker",
        "anecdote": "Sommigen gebruiken deze knowhow binnen een wettelijk kader, anderen zijn vaker outlaw."
      },
      {
        "id": 9,
        "question": "Welke software wordt gebruikt om op internet te surfen op een pc, tablet of smartphone ?",
        "propositions": [
          "Browsers",
          "Spreadsheets",
          "Redactie",
          "Emulatoren"
        ],
        "réponse": "Browsers",
        "anecdote": "De eerste stabiele en wijdverspreide browser was « NCSA Mosaic », in 1993."
      },
      {
        "id": 10,
        "question": "Met welke tool die is ontwikkeld door de gigant Google, kunt u uw planning beheren ?",
        "propositions": [
          "Google Mobile",
          "Google TimeLine",
          "Google Tempo",
          "Google Agenda"
        ],
        "réponse": "Google Agenda",
        "anecdote": "Met « Google Agenda » kunt u evenementen en agenda's delen en deze op internet of op een website publiceren."
      }
    ],
    "confirmé": [
      {
        "id": 11,
        "question": "Welk groot bedrijf kreeg in 2011 groen licht om « Skype » te kopen ?",
        "propositions": [
          "Appel",
          "Google",
          "Microsoft",
          "Facebook"
        ],
        "réponse": "Microsoft",
        "anecdote": "« Skype » is gratis software waarmee u telefoon- en videogesprekken via internet kunt voeren en het scherm kunt delen."
      },
      {
        "id": 12,
        "question": "Wat is waarschijnlijk de bekendste van de zogenaamde gratis computersystemen ?",
        "propositions": [
          "Mac OS",
          "Windows",
          "Linux",
          "MS-DOS"
        ],
        "réponse": "Linux",
        "anecdote": "Linux is een computersysteem dat draait op hardware variërend van mobiele telefoons tot supercomputers."
      },
      {
        "id": 13,
        "question": "Wat is de naam van de professionele Google-servicesoplossing ?",
        "propositions": [
          "Google Apps",
          "Google Serve",
          "Google Mac",
          "Google Pro"
        ],
        "réponse": "Google Apps",
        "anecdote": "Deze website voor bedrijven heeft veel applicaties online."
      },
      {
        "id": 14,
        "question": "Welk type software wordt gratis en vrij ter beschikking gesteld door de maker ?",
        "propositions": [
          "Software",
          "Freeware",
          "Malware",
          "Adware"
        ],
        "réponse": "Freeware",
        "anecdote": "Men moet echter freeware (freeware) en shareware (shareware) niet verwarren."
      },
      {
        "id": 15,
        "question": "Welke start-up Facebook kocht in april 2012 voor meer dan een miljard dollar ?",
        "propositions": [
          "Ventiel",
          "Backelite",
          "Instagram",
          "Globalnet"
        ],
        "réponse": "Instagram",
        "anecdote": "« Instagram » is een applicatie die in oktober 2010 mede is opgericht en gelanceerd door de Amerikaan Kevin Systrom en de Braziliaan Michel Mike Krieger."
      },
      {
        "id": 16,
        "question": "Welk woord wordt in Quebec vaak gebruikt om naar elektronische post te verwijzen ?",
        "propositions": [
          "Copitel",
          "E-mail",
          "Brief",
          "Emel"
        ],
        "réponse": "E-mail",
        "anecdote": "E-mail wordt meestal herkend als een geldige manier om contact met iemand op te nemen."
      },
      {
        "id": 17,
        "question": "Welke software die door Microsoft is gekocht, heeft « Windows Live Messenger » in 2013 vervangen ?",
        "propositions": [
          "Skype",
          "Instagram",
          "QuickTime",
          "Pidgin"
        ],
        "réponse": "Skype",
        "anecdote": "« Skype » werd in 2003 in Estland opgericht door Niklas Zennström en Janus Friis en ontwikkeld door drie Esten achter de software « KaZaA »."
      },
      {
        "id": 18,
        "question": "Wat was de naam van de vorige internetbrowser die « Microsoft Edge » werd ?",
        "propositions": [
          "Chrome",
          "Internet Explorer",
          "Safari",
          "Firefox"
        ],
        "réponse": "Internet Explorer",
        "anecdote": "Versie 11 van de « Internet Explorer » -browser zal nog steeds aanwezig zijn in Windows 10 vóór de geleidelijke overgang naar « Microsoft Edge »."
      },
      {
        "id": 19,
        "question": "Welke software is essentieel om uw computer op internet te beschermen ?",
        "propositions": [
          "Berichten",
          "Kat",
          "Antivirus",
          "Browser"
        ],
        "réponse": "Antivirus",
        "anecdote": "Antivirusprogramma's kunnen zowel de inhoud van een harde schijf als computer-RAM scannen."
      },
      {
        "id": 20,
        "question": "Wie is de allereerste paus die op « Twitter » post ?",
        "propositions": [
          "Francois",
          "Johannes Paulus II",
          "Paulus VI",
          "Benedictus XVI"
        ],
        "réponse": "Benedictus XVI",
        "anecdote": "De bekende conservatieve, kardinaal Ratzinger werd op 19 april 2005 gekozen om Johannes Paulus II op te volgen."
      }
    ],
    "expert": [
      {
        "id": 21,
        "question": "Welke e-mail die door Mozilla is gemaakt, is de ideale partner voor de « Firefox » browser ?",
        "propositions": [
          "Incredimail",
          "Foxmail",
          "Thunderbird",
          "Sylpheed"
        ],
        "réponse": "Thunderbird",
        "anecdote": "Net als « Firefox », is « Thunderbird » en zijn XUL-interface gebaseerd op de Gecko-engine."
      },
      {
        "id": 22,
        "question": "Hoe heet de online kantoorsuite die door Microsoft wordt aangeboden ?",
        "propositions": [
          "StarOffice",
          "KOffice",
          "OpenOffice",
          "Office 365"
        ],
        "réponse": "Office 365",
        "anecdote": "Met « Office 365 » -abonnementen voor individuen kunt u profiteren van de volledige versie van de Office-suite die we kennen."
      },
      {
        "id": 23,
        "question": "Wat was de codenaam voor Microsoft Windows versie 3.1 ?",
        "propositions": [
          "Opus",
          "Janus",
          "Startus",
          "Uranus"
        ],
        "réponse": "Janus",
        "anecdote": "Versie 3 was de eerste die een groot succes boekte, waardoor Microsoft kon concurreren met de Apple Macintosh."
      },
      {
        "id": 24,
        "question": "Wat is de naam van de online opslagservice van Windows Live ?",
        "propositions": [
          "Dropbox",
          "RapidShare",
          "MediaFire",
          "Onedrive"
        ],
        "réponse": "Onedrive",
        "anecdote": "Deze online opslag- en applicatieservice, opgericht in 2007, is een manifestatie van het concept van cloud computing."
      },
      {
        "id": 25,
        "question": "Wat is de nieuwe naam van de gratis instant messaging-software « Gaim » ?",
        "propositions": [
          "iShare",
          "Pidgin",
          "Connect",
          "Komunnity"
        ],
        "réponse": "Pidgin",
        "anecdote": "« Gaim » is in 2007 hernoemd tot « Pidgin » vanwege klachten van AOL en het merk AIM."
      },
      {
        "id": 26,
        "question": "Welke softwaresuite is gelijk aan Microsoft Office bij de gigantische Google ?",
        "propositions": [
          "Google-documenten",
          "Google Sites",
          "OpenOffice",
          "Werkt"
        ],
        "réponse": "Google-documenten",
        "anecdote": "« Google Documenten » is een voortzetting van de evoluties van « Google Spreadsheets » en « Writely », tekstverwerkingssoftware."
      },
      {
        "id": 27,
        "question": "Uit welk land komt het gratis « Opera » -softwarepakket ?",
        "propositions": [
          "Oostenrijk",
          "Frankrijk",
          "Italië",
          "Noorwegen"
        ],
        "réponse": "Noorwegen",
        "anecdote": "« Opera » is een webbrowser die is ontwikkeld door het Noorse bedrijf Opera Software, dat verschillende internetgerelateerde software aanbiedt."
      },
      {
        "id": 28,
        "question": "Met welke van deze tools kunt u webpagina's niet bekijken ?",
        "propositions": [
          "Mozilla Firefox",
          "Google Chrome",
          "Internet Explorer",
          "Acrobat Reader"
        ],
        "réponse": "Acrobat Reader",
        "anecdote": "Adobe verandert regelmatig de naam van de producten van de Acrobat-familie en dit door het assortiment onder te verdelen."
      },
      {
        "id": 29,
        "question": "Hoeveel downloads waren er eind 2012 in de beroemde « App Store » ?",
        "propositions": [
          "5 miljard",
          "25 miljard",
          "35 miljard",
          "15 miljard"
        ],
        "réponse": "35 miljard",
        "anecdote": "Sinds de update van het besturingssysteem van Apple iOS 7 in september 2013 heeft de « App Store » een compleet nieuw ontwerp."
      },
      {
        "id": 30,
        "question": "Wat is de officiële aanmaakdatum van « Wikipedia » in het Frans ?",
        "propositions": [
          "8 december 2000",
          "2 januari 1999",
          "15 januari 2002",
          "23 maart 2001"
        ],
        "réponse": "23 maart 2001",
        "anecdote": "Er zijn verschillende manieren om de encyclopedie te raadplegen, zoals spiegelwebsites of smartphone-applicaties."
      }
    ]
    }
  }
}

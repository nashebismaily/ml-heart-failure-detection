import pickle

model = pickle.load(open('rf_classifier.pkl', 'rb'))

def predict(args):
  age = float(args.get('age'))
  anaemia = int(args.get('anaemia'))
  creatinine_phosphokinase = float(args.get('creatinine_phosphokinase'))
  diabetes = int(args.get('diabetes'))
  ejection_fraction = int(args.get('ejection_fraction'))
  high_blood_pressure = int(args.get('high_blood_pressure'))
  platelets = float(args.get('platelets'))
  serum_creatinine = float(args.get('serum_creatinine'))
  serum_sodium = int(args.get('serum_sodium'))
  sex = int(args.get('sex'))
  smoking = int(args.get('smoking'))
  time = int(args.get('time'))

  result = model.predict([[age,
                           anaemia,
                           creatinine_phosphokinase,
                           diabetes,ejection_fraction,
                           high_blood_pressure,
                           platelets,
                           serum_creatinine,
                           serum_sodium,
                           sex,
                           smoking,
                           time]])
  if result[0] == 1:
    return "Patient Has Heart Failure Risk!"
  else:
    return "No Heart Failure Risk Detected"

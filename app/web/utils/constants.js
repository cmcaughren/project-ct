export const MFPEFormData = {
    patient_rfid: '',
    document_num: '',
    location: "Main Medical",
    handover_from: '',
    arrival_date: new Date,
    arrival_time: new Date,
    triage_acuity: '',
    age: new Number,
    gender: '',
    on_shift: '',
    chief_complaints: [],
    chief_complaint_other: '',
    arrival_method: '',
    handover_too: '',
    departure_time: null,
    departure_date: null,
    departure_dest: '',
    comment: '',
};

export const chiefComplaints = [
    'Abdominal Pain',
    'Adverse Drug Effect',
    'Agitation' ,
    'Allergic Reaction',
    'Anxiety' ,
    'Bizarre Behaviour' ,
    'Chest Pain' ,
    'Dizziness/Presyncope/Lightheaded',
    'Hallucinations' ,
    'Headache' ,
    'Loss of Consciousness',
    'Nausea/Vomiting',
    'Other',
    'Other Pain',
    'Seizure',
    'Shortness of Breath',
    'Trauma',
];
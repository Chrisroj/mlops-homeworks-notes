import pickle

from flask import Flask, request, jsonify

# Load Model
model_name = "model2.bin"
dv_name = "dv.bin"

with open(model_name, "rb") as f_in:
    model = pickle.load(f_in)
with open(dv_name, "rb") as f_in:
    dv = pickle.load(f_in)

# Flask App
app = Flask("churn-app-h5")

def predict_proba(customer):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)
    churn_proba = y_pred[0][1]
    
    return churn_proba
    
@app.route("/predict_churn", methods = ["POST"])
def predict_post():
    customer = request.get_json()
    
    churn_proba = predict_proba(customer)
    churn_bool = churn_proba >= 0.5
    
    result = {
        "churn_proba": float(churn_proba),
        "churn_bool": bool(churn_bool)
    }
    
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port = 7878)

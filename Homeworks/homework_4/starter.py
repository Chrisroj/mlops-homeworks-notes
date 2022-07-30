import sys
import pickle
import pandas as pd

def load_model(model_path: str = 'model.bin'):
    with open(model_path, 'rb') as f_in:
        dv, lr = pickle.load(f_in)
    return dv, lr

def read_data(filename, year, month):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.dropOff_datetime - df.pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()
    
    categorical = ['PUlocationID', 'DOlocationID']
    
    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')
    return df

def preprocessing(df, dv):
    categorical = ['PUlocationID', 'DOlocationID']
    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    
    return X_val

def save_results(df, y_pred, output_file):
    df_result = pd.DataFrame()
    df_result['ride_id'] = df['ride_id']
    df_result['predicted_duration'] = y_pred

    df_result.to_parquet(
        output_file,
        engine='pyarrow',
        compression=None,
        index=False
    )

def run():
    year = int(sys.argv[1]) # 2021
    month = int(sys.argv[2]) # 2
    
    input_file = f'https://nyc-tlc.s3.amazonaws.com/trip+data/fhv_tripdata_{year:04d}-{month:02d}.parquet'
    output_file = f'output/results_fhv_tripdata_{year:04d}-{month:02d}.parquet'
    model_path = "model.bin"
    
    print(f"Reading Data: {input_file}")
    df = read_data(input_file, year, month)
    
    print(f"Loading Model: {model_path}")
    dv, lr = load_model(model_path)
    
    print(f"Preprocessing Data")
    X_val = preprocessing(df, dv)
    
    print(f"Doing Prediction")
    y_pred = lr.predict(X_val)
    print(f"Mean Predicted Time: {y_pred.mean()}")
    
    print(f"Saving Results")
    save_results(df, y_pred, output_file)

if __name__ == '__main__':
    run()

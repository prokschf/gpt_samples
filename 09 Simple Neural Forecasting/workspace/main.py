from temperature_predictor import TemperaturePredictor

def main():
    sequence = [25, 26, 27, 26, 24, 21]
    predictor = TemperaturePredictor(sequence)
    predictor.train()
    predictions = predictor.predict()
    print(predictions)

if __name__ == "__main__":
    main()

import joblib

from data_preprocessing import (
    load_invoice_data,
    apply_labels,
    split_data,
    scale_features
)

from model_evaluation import (
    train_random_forest,
    evaluate_classifier
)


def main():

    # Load data
    df = load_invoice_data()

    # Create labels
    df = apply_labels(df)

    FEATURES = [
        "invoice_quantity",
        "invoice_dollars",
        "Freight",
        "days_po_to_invoice",
        "days_to_pay",
        "total_brands",
        "total_item_quantity",
        "total_item_dollars",
        "avg_receiving_delay"
    ]

    TARGET = "flag_invoice"

    # Split data
    X_train, X_test, y_train, y_test = split_data(
        df,
        FEATURES,
        TARGET
    )

    # Scale features
    X_train_scaled, X_test_scaled = scale_features(
        X_train,
        X_test
    )

    # Train model
    grid_search = train_random_forest(
        X_train_scaled,
        y_train
    )

    # Evaluate
    evaluate_classifier(
        grid_search.best_estimator_,
        X_test_scaled,
        y_test,
        "Random Forest Classifier"
    )

    # Save model
    joblib.dump(
        grid_search.best_estimator_,
        "models/predict_flag_invoice.pkl"
    )

    print("\nModel Saved Successfully")
    
if __name__ == "__main__":
    main()
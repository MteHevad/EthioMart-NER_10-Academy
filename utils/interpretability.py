# utils/interpretability.py
import shap
import lime.lime_tabular

def explain_with_shap(model, X):
    """Explain model predictions using SHAP."""
    explainer = shap.Explainer(model)
    shap_values = explainer(X)
    return shap_values

def explain_with_lime(model, X, feature_names):
    """Explain model predictions using LIME."""
    explainer = lime.lime_tabular.LimeTabularExplainer(X, feature_names=feature_names)
    return explainer

# Example function to visualize SHAP values
def plot_shap_values(shap_values):
    """Visualize SHAP values."""
    shap.summary_plot(shap_values)

package main.java.com.shared.pipeline;

public interface PaymentProcessStep {
    String getStepName();  // e.g., "DECRYPT", "TRANSFORM"
    String execute(String message);
}
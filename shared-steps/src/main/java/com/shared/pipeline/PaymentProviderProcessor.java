package com.shared.pipeline;

import java.util.List;

import main.java.com.shared.pipeline.PaymentProcessStep;

public class PaymentProviderProcessor {
    private final List<PaymentProcessStep> steps;

    public PaymentProviderProcessor(List<PaymentProcessStep> steps) {
        this.steps = steps;
    }

    public String process(String input) {
        String result = input;
        for (PaymentProcessStep step : steps) {
            result = step.execute(result);
        }
        return result;
    }
}
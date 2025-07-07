
package com.shared;
import org.springframework.stereotype.Component;

import main.java.com.shared.pipeline.PaymentProcessStep;

@Component("decrypt")
public class DecryptStep implements PaymentProcessStep
 {
    public String execute(String input) {
        return "[DECRYPTED] " + input;
    }
}


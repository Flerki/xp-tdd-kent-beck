package com.amairovi;

public abstract class Money {
    protected int amount;

    @Override
    public boolean equals(Object obj) {
        Money money = (Money) obj;
        return amount == money.amount && getClass().equals(money.getClass());
    }

    static Dollar dollar(int amount) {
        return new Dollar(amount);
    }

    static Franc franc(int amount) {
        return new Franc(amount);
    }

    public abstract Money times(int multiplier);
}

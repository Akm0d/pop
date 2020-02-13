# -*- coding: utf-8 -*-

# Import pop
import pop.hub
import pytest


def test_contract_context():
    hub = pop.hub.Hub()
    hub.pop.sub.add(
        pypath="tests.mods.contract_ctx",
        subname="mods",
        contracts_pypath="tests.contracts",
    )
    assert hub.mods.ctx.test() == "contract executed"
    # Multiple calls have the same outcome
    assert hub.mods.ctx.test() == "contract executed"


def test_contract_context_update_call():
    # if a pre modifies args, make sure they persist when called via 'call' function
    hub = pop.hub.Hub()
    hub.pop.sub.add(
        pypath="tests.mods.contract_ctx",
        subname="mods",
        contracts_pypath="tests.contracts",
    )
    assert hub.mods.ctx_update.test_call(True) == "contract executed"
    # Multiple calls have the same outcome
    assert hub.mods.ctx_update.test_call(True) == "contract executed"


def test_contract_context_update_direct():
    # if a pre modifies args, make sure they persist when called directly
    hub = pop.hub.Hub()
    hub.pop.sub.add(
        pypath="tests.mods.contract_ctx",
        subname="mods",
        contracts_pypath="tests.contracts",
    )
    assert hub.mods.ctx_update.test_direct(True) is False
    assert hub.mods.ctx_update.test_direct(True) is False


def test_contract_ctx_argument_retrieval():
    hub = pop.hub.Hub()
    hub.pop.sub.add(
        pypath="tests.mods.contract_ctx",
        subname="mods",
        contracts_pypath="tests.contracts",
    )
    assert hub.mods.ctx_args.test("yes", yes=True) is True
    assert hub.mods.ctx_args.test("yes", yes=False) is False
    assert hub.mods.ctx_args.test("no", no=False) is False
    assert hub.mods.ctx_args.test("no", no=True) is True

    with pytest.raises(
        pop.exc.BindError, match="got an unexpected keyword argument 'garbage'"
    ):
        hub.mods.ctx_args.test("", garbage=True)

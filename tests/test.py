""" api tests """


import json


def test_works(client):
    rv = client.get("/ping")
    res = json.loads(rv.data)

    assert rv.status == "200 OK"
    assert res["status"] == "ok"


def test_get_member_by_id(client, member_fixture):
    """ test get member by id """
    test_member = member_fixture({"mem_id": 42, "phone": "5552223333"})

    rv = client.get(f"/member?id={test_member.id}")
    res = json.loads(rv.data)

    assert rv.status == "200 OK"
    assert len(res["members"]) == 1
    assert res["members"][0]["mem_id"] == 42


def test_get_member_by_memid(client, member_fixture):
    """ test get member by memid """
    test_member = member_fixture({"mem_id": 42, "phone": "5552223333"})

    rv = client.get(f"/member?mem_id={test_member.mem_id}")
    res = json.loads(rv.data)

    assert rv.status == "200 OK"
    assert len(res["members"]) == 1
    assert res["members"][0]["mem_id"] == 42


def test_get_member_by_phone(client, member_fixture):
    """ test get member by memid """
    test_member = member_fixture(
        {"mem_id": 1212, "phone": "8185551122", "fname": "Test", "lname": "Testing"}
    )

    rv = client.get(f"/member?phone={test_member.phone}")
    res = json.loads(rv.data)

    assert rv.status == "200 OK"
    assert len(res["members"]) == 1
    assert res["members"][0]["mem_id"] == 1212


def test_get_multiple(client, member_fixture):
    create_members = [member_fixture({"mem_id": x}) for x in (12, 13, 14, 15)]
    test_mem_ids = [m.mem_id for m in create_members]

    qs = ",".join(str(_id) for _id in test_mem_ids)

    rv = client.get(f"/member?mem_id={qs}")
    res = json.loads(rv.data)

    assert rv.status == "200 OK"
    assert len(res["members"]) == 4
    assert res["members"][0]["mem_id"] == 12
    assert res["members"][1]["mem_id"] == 13
    assert res["members"][2]["mem_id"] == 14
    assert res["members"][3]["mem_id"] == 15


def test_create_member(client, member_fixture):
    new_member = {
        "mem_id": 88,
        "fname": "Create",
        "lname": "Test",
        "phone": "5550012211",
    }
    rv = client.post(f"/member", json={"members": [new_member]})
    res = json.loads(rv.data)

    assert rv.status == "200 OK"
    assert len(res["members"]) == 1

    # get the new member
    rv = client.get(f"/member?mem_id={res['members'][0]['mem_id']}")
    res = json.loads(rv.data)

    assert rv.status == "200 OK"
    assert len(res["members"]) == 1
    assert res["members"][0]["mem_id"] == 88

import logging


def test_warns_when_count_below_threshold(caplog):
    from dags.dag_crawl import check_count_anomaly

    with caplog.at_level(logging.WARNING):
        result = check_count_anomaly("airline", 3)  # 阈值是15,3远低于它

    assert result is True
    assert "抓取数量疑似异常" in caplog.text
    assert "airline" in caplog.text


def test_no_warning_when_count_above_threshold(caplog):
    from dags.dag_crawl import check_count_anomaly

    with caplog.at_level(logging.WARNING):
        result = check_count_anomaly("airline", 50)  # 远高于阈值15

    assert result is False
    assert "抓取数量疑似异常" not in caplog.text


def test_unknown_review_type_uses_default_threshold(caplog):
    from dags.dag_crawl import check_count_anomaly, DEFAULT_MIN_THRESHOLD

    with caplog.at_level(logging.WARNING):
        result = check_count_anomaly("some_new_type_not_in_dict", DEFAULT_MIN_THRESHOLD - 1)

    assert result is True
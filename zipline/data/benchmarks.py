#
# Copyright 2013 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logbook

import pandas as pd
from trading_calendars import get_calendar

log = logbook.Logger(__name__)


def get_benchmark_returns_from_file(filelike):
    """
    Get a Series of benchmark returns from a file

    Parameters
    ----------
    filelike : str or file-like object
        Path to the benchmark file.
        expected csv file format:
        date,return
        2020-01-02 00:00:00+00:00,0.01
        2020-01-03 00:00:00+00:00,-0.02

    """
    log.info("Reading benchmark returns from {}", filelike)

    df = pd.read_csv(
        filelike,
        index_col=['date'],
        parse_dates=['date'],
    ).tz_localize('utc')

    if 'return' not in df.columns:
        raise ValueError("The column 'return' not found in the "
                         "benchmark file \n"
                         "Expected benchmark file format :\n"
                         "date, return\n"
                         "2020-01-02 00:00:00+00:00,0.01\n"
                         "2020-01-03 00:00:00+00:00,-0.02\n")

    return df['return'].sort_index()


def get_benchmark_returns(symbol, start, end):
    """
    Get a Series of benchmark returns from Yahoo associated with `symbol`.
    Default is `SPY`.
    Parameters
    ----------
    symbol : str
        Benchmark symbol for which we're getting the returns.
    The data is provided by Yahoo Finance
    """
    cal = get_calendar('NYSE')
    dates = cal.sessions_in_range(start, end)
    data = pd.DataFrame(0.0, index=dates, columns=['close'])
    data = data['close']
    return data.sort_index().iloc[1:]

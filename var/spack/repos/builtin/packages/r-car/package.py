# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RCar(RPackage):
    """Functions and Datasets to Accompany J. Fox and S. Weisberg, An R
    Companion to Applied Regression, Second Edition, Sage, 2011."""

    homepage = "https://r-forge.r-project.org/projects/car/"
    url      = "https://cloud.r-project.org/src/contrib/car_2.1-4.tar.gz"
    list_url = "https://cloud.r-project.org/src/contrib/Archive/car"

    version('3.0-3', sha256='fa807cb12f6e7fb38ec534cac4eef54747945c2119a7d51155a2492ad778c36f')
    version('3.0-2', sha256='df59a9ba8fed67eef5ddb8f92f2b41745df715d5695c71d562d7031513f37c50')
    version('2.1-4', 'a66c307e8ccf0c336ed197c0f1799565')
    version('2.1-2', '0f78ad74ef7130126d319acec23951a0')

    depends_on('r@3.2.0:', when='@:3.0-2', type=('build', 'run'))
    depends_on('r@3.5.0:', when='@3.0-3:', type=('build', 'run'))
    depends_on('r-cardata@3.0-0:', when='@3.0:', type=('build', 'run'))
    depends_on('r-abind', when='@3.0:', type=('build', 'run'))
    depends_on('r-mass', type=('build', 'run'))
    depends_on('r-mgcv', type=('build', 'run'))
    depends_on('r-nnet', type=('build', 'run'))
    depends_on('r-pbkrtest@0.4-4:', type=('build', 'run'))
    depends_on('r-quantreg', type=('build', 'run'))
    depends_on('r-maptools', when='@3.0:', type=('build', 'run'))
    depends_on('r-rio', when='@3.0:', type=('build', 'run'))
    depends_on('r-lme4', when='@3.0:', type=('build', 'run'))
    depends_on('r-nlme', when='@3.0:', type=('build', 'run'))

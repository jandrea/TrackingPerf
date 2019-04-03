import FWCore.ParameterSet.Config as cms

from RecoLocalTracker.Configuration.RecoLocalTracker_cff import *
from SimGeneral.TrackingAnalysis.simHitTPAssociation_cfi import *
from SimTracker.TrackerHitAssociation.tpClusterProducer_cfi import *
from SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi import *

from RecoTracker.TransientTrackingRecHit.TTRHBuilders_cff import *
from RecoLocalTracker.SiPixelRecHits.PixelCPEGeneric_cfi import *
from SimTracker.TrackAssociation.LhcParametersDefinerForTP_cfi import *

# Track Associators
from SimTracker.TrackAssociatorProducers.trackAssociatorByHits_cfi import *



process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

#
#process.load('Configuration.StandardSequences.Reconstruction_cff')
#
#process.load('Configuration.Geometry.GeometryRecoDB_cff')
#process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
#
#process.load("RecoTracker.TrackProducer.TrackRefitters_cff") 
#process.load("Configuration.StandardSequences.MagneticField_cff")
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.GlobalTag.globaltag = '92X_upgrade2017_realistic_v7'  
#

#process.GlobalTag.globaltag = cms.string('auto')



process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = '92X_upgrade2017_realistic_v7'  


### standard includes
process.load('Configuration/StandardSequences/Services_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load("Configuration.StandardSequences.RawToDigi_cff")
process.load("Configuration.EventContent.EventContent_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")

### validation-specific includes
process.load("SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi")
process.load("SimTracker.TrackAssociation.trackingParticleRecoTrackAsssociation_cfi")
process.load("Validation.RecoTrack.MultiTrackValidatorGenPs_cfi")
process.load("DQMServices.Components.EDMtoMEConverter_cff")
process.load("Validation.Configuration.postValidation_cff")
process.quickTrackAssociatorByHits.SimToRecoDenominator = cms.string('reco')

process.load("SimTracker.TrackAssociatorProducers.trackAssociatorByChi2_cfi")
process.trackAssociatorByChi2.chi2cut = cms.double(500.0)


process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
 

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
 

 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17DRPremix/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/GEN-SIM-RECODEBUG/92X_upgrade2017_realistic_v10_ext1-v2/50004/8A1B91E4-479A-E711-87F4-0CC47AC08BC8.root',
 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17DRPremix/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/GEN-SIM-RECODEBUG/92X_upgrade2017_realistic_v10_ext1-v2/50002/EAF7246B-509A-E711-814F-0CC47A706D26.root',
 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17DRPremix/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/GEN-SIM-RECODEBUG/92X_upgrade2017_realistic_v10_ext1-v2/50005/102B9E0A-619A-E711-83D9-0CC47A706CDE.root',
 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17DRPremix/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/GEN-SIM-RECODEBUG/92X_upgrade2017_realistic_v10_ext1-v2/50004/9E1B0ED5-529A-E711-9BB1-0CC47A7034D2.root',
 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17DRPremix/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/GEN-SIM-RECODEBUG/92X_upgrade2017_realistic_v10_ext1-v2/50005/569E6FC1-479A-E711-A7B0-002590DE6C96.root',
 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17DRPremix/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/GEN-SIM-RECODEBUG/92X_upgrade2017_realistic_v10_ext1-v2/50005/427D51BE-579A-E711-BEE8-0CC47AC08B24.root',
 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17DRPremix/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/GEN-SIM-RECODEBUG/92X_upgrade2017_realistic_v10_ext1-v2/50002/9634764E-569A-E711-B073-C45444922D3C.root',
 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17DRPremix/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/GEN-SIM-RECODEBUG/92X_upgrade2017_realistic_v10_ext1-v2/50002/3ECFE4C3-529A-E711-B5ED-0CC47AC08C1A.root',
 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17DRPremix/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/GEN-SIM-RECODEBUG/92X_upgrade2017_realistic_v10_ext1-v2/50002/08F36344-569A-E711-AC2A-C454449229AF.root',
 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17DRPremix/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/GEN-SIM-RECODEBUG/92X_upgrade2017_realistic_v10_ext1-v2/50001/E07B1781-469A-E711-9976-0CC47A706D26.root',
 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17DRPremix/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/GEN-SIM-RECODEBUG/92X_upgrade2017_realistic_v10_ext1-v2/50001/D238F3FE-569A-E711-92E4-0CC47AC08BC8.root',
 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17DRPremix/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/GEN-SIM-RECODEBUG/92X_upgrade2017_realistic_v10_ext1-v2/50001/C4FA00C0-479A-E711-9480-0CC47A703326.root',
 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17DRPremix/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/GEN-SIM-RECODEBUG/92X_upgrade2017_realistic_v10_ext1-v2/50001/B2546A50-569A-E711-9738-0CC47AC08C34.root',
 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17DRPremix/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/GEN-SIM-RECODEBUG/92X_upgrade2017_realistic_v10_ext1-v2/50001/1C739FC5-509A-E711-93BE-0CC47AC08904.root',
 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17DRPremix/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/GEN-SIM-RECODEBUG/92X_upgrade2017_realistic_v10_ext1-v2/50001/0236B9E3-4C9A-E711-8878-0CC47A706FFE.root',
 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17DRPremix/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/GEN-SIM-RECODEBUG/92X_upgrade2017_realistic_v10_ext1-v2/50005/780ED8B7-479A-E711-9A49-0CC47AC08C1A.root',
 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17DRPremix/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/GEN-SIM-RECODEBUG/92X_upgrade2017_realistic_v10_ext1-v2/50005/DEF51660-5E9A-E711-B7B3-0CC47AC08C34.root',
 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17DRPremix/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/GEN-SIM-RECODEBUG/92X_upgrade2017_realistic_v10_ext1-v2/50005/D4A25F82-5A9A-E711-BC24-0025901D40A6.root',
 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17DRPremix/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/GEN-SIM-RECODEBUG/92X_upgrade2017_realistic_v10_ext1-v2/50005/CABEC298-4C9A-E711-BA5E-0CC47A706CDE.root',
 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17DRPremix/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/GEN-SIM-RECODEBUG/92X_upgrade2017_realistic_v10_ext1-v2/50005/8E208FAC-559A-E711-96EE-002590DE6C96.root',
 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17DRPremix/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/GEN-SIM-RECODEBUG/92X_upgrade2017_realistic_v10_ext1-v2/50005/569F4F24-599A-E711-99BB-0CC47A703326.root'



    )
)


process.TFileService = cms.Service("TFileService", fileName = cms.string("trackingNTuple.root") )



process.load("SimTracker.TrackAssociation.trackingParticleRecoTrackAsssociation_cfi")

from CommonTools.RecoAlgos.trackingParticleRefSelector_cfi import trackingParticleRefSelector as _trackingParticleRefSelector
process.trackingParticlesIntime = _trackingParticleRefSelector.clone(
    signalOnly = False,
    intimeOnly = False,
    chargedOnly = True,
    tip = 1e5,
    lip = 1e5,
    minRapidity = -2.4,
    maxRapidity =  2.4,
    ptMin = 1,
)


process.load("SimGeneral.MixingModule.mixNoPU_cfi")
process.load("SimGeneral.MixingModule.trackingTruthProducerSelection_cfi")

process.trackingParticles.simHitCollections = cms.PSet( )
process.mix.playback = cms.untracked.bool(True)
process.mix.digitizers = cms.PSet(
     mergedtruth = cms.PSet(process.trackingParticles)
)
for a in process.aliases: delattr(process, a)


#process.load("SimGeneral.TrackingAnalysis.simHitTPAssociation_cfi")
#
#process.load("SimTracker.TrackerHitAssociation.tpClusterProducer_cfi")
#process.load("SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi")
#process.load("SimTracker.TrackAssociatorProducers.trackAssociatorByHits_cfi")
#process.load("SimTracker.TrackAssociation.trackingParticleRecoTrackAsssociation_cfi")
#process.load("SimG4Core.Application.g4SimHits_cfi")


process.trackingPerf = cms.EDAnalyzer('TrackingPerf',
      tracks               = cms.untracked.InputTag('generalTracks'),
      trackLabel           = cms.InputTag('generalTracks'),
      #trackAssociator      = cms.untracked.InputTag('trackingParticleRecoTrackAsssociation'),
      #trackAssociator      = cms.untracked.InputTag('trackAssociatorByHits'),
      trackAssociator      = cms.untracked.InputTag('quickTrackAssociatorByHits'),
      beamSpot             = cms.untracked.InputTag('offlineBeamSpot'),
      parametersDefiner    = cms.untracked.string('LhcParametersDefinerForTP'),
      #trackingParticles    = cms.untracked.InputTag('trackingParticlesIntime'),
      trackingParticles    = cms.untracked.InputTag('trackingParticlesIntime'),
      trackingParticlesRef = cms.untracked.bool(True),
      TTRHBuilder          = cms.string('WithTrackAngle'),
      useCluster           = cms.untracked.bool(False),
      vertices             = cms.untracked.InputTag('offlinePrimaryVertices'),
      jetInput             = cms.InputTag('ak4PFJets')
)


##process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
##process.load("SimGeneral.MixingModule.mixNoPU_cfi")
#process.load("Configuration.StandardSequences.Simulation_cff")
#
#
#process.load("Geometry.CMSCommonData.cmsExtendedGeometryXML_cfi")
##process.load("SimTransport.HectorProducer.HectorTransport_cfi")
#
#
#
#process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
#	g4SimHits = cms.PSet(
#   		 initialSeed = cms.untracked.uint32(123456789),
#    		 engineName = cms.untracked.string('TRandom3')
#  	),
#  	LHCTransport = cms.PSet(
#    		initialSeed = cms.untracked.uint32(321456789),
#    		engineName = cms.untracked.string('TRandom3')
#  	)
#
#)
 
#process.simHitTPAssocProducer.simHitSrc = cms.VInputTag( 
#	cms.InputTag('g4SimHits','TrackerHitsTIBLowTof'),
#	cms.InputTag('g4SimHits','TrackerHitsTIBHighTof'),
#	cms.InputTag('g4SimHits','TrackerHitsTIDLowTof'),
#	cms.InputTag('g4SimHits','TrackerHitsTIDHighTof'),
#	cms.InputTag('g4SimHits','TrackerHitsTOBLowTof'),
#	cms.InputTag('g4SimHits','TrackerHitsTOBHighTof'),
#	cms.InputTag('g4SimHits','TrackerHitsTECLowTof'),
#	cms.InputTag('g4SimHits','TrackerHitsTECHighTof'),
#	cms.InputTag( 'g4SimHits','TrackerHitsPixelBarrelLowTof'),
#	cms.InputTag('g4SimHits','TrackerHitsPixelBarrelHighTof'),
#	cms.InputTag('g4SimHits','TrackerHitsPixelEndcapLowTof'),
#	cms.InputTag('g4SimHits','TrackerHitsPixelEndcapHighTof') 
#	)


#process.p = cms.Path(trackingParticlesIntime*simHitTPAssocProducer*tpClusterProducer*process.trackingPerf)
process.p = cms.Path( 
	#process.LHCTransport*
	#process.g4SimHits*
	process.mix *
	#process.simHitTPAssocProducer*
	process.tpClusterProducer*
	process.quickTrackAssociatorByHits*
	process.trackingParticleRecoTrackAsssociation*
	process.trackingParticlesIntime*
	process.trackingPerf)












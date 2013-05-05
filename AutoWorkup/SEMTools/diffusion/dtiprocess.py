# -*- coding: utf8 -*-
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

from nipype.interfaces.base import CommandLine, CommandLineInputSpec, SEMLikeCommandLine, TraitedSpec, File, Directory, traits, isdefined, InputMultiPath, OutputMultiPath
import os


class dtiaverageInputSpec(CommandLineInputSpec):
    method = traits.Enum("euclidean", "log-euclidean", "pga", desc="Statistics method (euclidean,log-euclidean,pga)", argstr="--method %s")
    verbose = traits.Bool(desc="produce verbose output", argstr="--verbose ")
    tensor_output = traits.Either(traits.Bool, File(), hash_files=False, desc="Averaged tensor volume", argstr="--tensor_output %s")
    inputs = InputMultiPath(File(exists=True), desc="List of all the tensor fields to be averaged", argstr="--inputs %s...")


class dtiaverageOutputSpec(TraitedSpec):
    tensor_output = File(desc="Averaged tensor volume", exists=True)


class dtiaverage(SEMLikeCommandLine):
    """title: DTIAverage

category: Diffusion.DTIProcess

description:
dtiaverage is a program that allows to compute the average of an arbitrary number of tensor fields (listed after the --inputs option) This program is used in our pipeline as the last step of the atlas building processing. When all the tensor fields have been deformed in the same space, to create the average tensor field (--tensor_output) we use dtiaverage.
 Several average method can be used (specified by the --method option): euclidian, log-euclidian and pga. The default being euclidian.

version: 1.0.0

documentation-url: http://www.google.com/

license:
    Copyright (c)  Casey Goodlett. All rights reserved.
    See http://www.ia.unc.edu/dev/Copyright.htm for details.
    This software is distributed WITHOUT ANY WARRANTY; without even
    the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
    PURPOSE.  See the above copyright notices for more information.


contributor: Casey Goodlett

"""

    input_spec = dtiaverageInputSpec
    output_spec = dtiaverageOutputSpec
    _cmd = " dtiaverage "
    _outputs_filenames = {'tensor_output':'tensor_output.nii'}


class dtiestimInputSpec(CommandLineInputSpec):
    brain_mask = File(desc="Brain mask.  Image where for every voxel == 0 the tensors are not estimated.", exists=True, argstr="--brain_mask %s")
    B0_mask_output = traits.Either(traits.Bool, File(), hash_files=False, desc="B0 mask used for the estimation. B0 thresholded either with the -t option value or the automatic OTSU value.", argstr="--B0_mask_output %s")
    bad_region_mask = File(desc="Bad region mask.  Image where for every voxel > 0 the tensors are not estimated.", exists=True, argstr="--bad_region_mask %s")
    threshold = traits.Int(desc="Baseline threshold for estimation. If not specified calculated using an OTSU threshold on the baseline image.", argstr="--threshold %d")
    B0 = traits.Either(traits.Bool, File(), hash_files=False, desc="Baseline image, average of all baseline images.", argstr="--B0 %s")
    idwi = traits.Either(traits.Bool, File(), hash_files=False, desc="idwi output image. Image with isotropic diffusion-weighted information = geometric mean of diffusion images.", argstr="--idwi %s")
    dwi_image = File(desc="DWI image volume (required)", exists=True, argstr="--dwi_image %s")
    tensor_output = traits.Either(traits.Bool, File(), hash_files=False, desc="Tensor OutputImage.", argstr="--tensor_output %s")
    method = traits.Enum("lls", "wls", "nls", "ml", desc="Esitmation method (lls,wls,nls,ml)", argstr="--method %s")
    weight_iterations = traits.Int(desc="Number of iterations to recaluate weightings from tensor estimate", argstr="--weight_iterations %d")
    step = traits.Float(desc="Gradient descent step size (for nls and ml methods)", argstr="--step %f")
    sigma = traits.Float(argstr="--sigma %f")
    verbose = traits.Bool(desc="produce verbose output", argstr="--verbose ")


class dtiestimOutputSpec(TraitedSpec):
    B0_mask_output = File(desc="B0 mask used for the estimation. B0 thresholded either with the -t option value or the automatic OTSU value.", exists=True)
    B0 = File(desc="Baseline image, average of all baseline images.", exists=True)
    idwi = File(desc="idwi output image. Image with isotropic diffusion-weighted information = geometric mean of diffusion images.", exists=True)
    tensor_output = File(desc="Tensor OutputImage.", exists=True)


class dtiestim(SEMLikeCommandLine):
    """title: dtiestim

category: Diffusion.DTIProcess

description:
dtiestim is a tool that takes in a set of DWIs (with --dwi_image option) in nrrd format and estimates a tensor field out of it. The output tensor file name is specified with the --tensor_output option
There are several methods to estimate the tensors which you can specify with the option --method lls|wls|nls|ml . Here is a short description of the different methods:
  lls Linear least squares. Standard estimation technique that recovers the tensor parameters by multiplying the log of the normalized signal intensities by the pseudo-inverse of the gradient matrix. Default option.
  wls Weighted least squares. This method is similar to the linear least squares method except that the gradient matrix is weighted by the original lls estimate. (See Salvador, R., Pena, A., Menon, D. K., Carpenter, T. A., Pickard, J. D., and Bullmore, E. T. Formal characterization and extension of the linearized diffusion tensor model. Human Brain Mapping 24, 2 (Feb. 2005), 144-155. for more information on this method). This method is recommended for most applications. The weight for each iteration can be specified with the --weight_iterations.  It is not currently the default due to occasional matrix singularities.
  nls Non-linear least squares. This method does not take the log of the signal and requires an optimization based on levenberg-marquadt to optimize the parameters of the signal. The lls estimate is used as an initialization. For this method the step size can be specified with the --step option.
  ml Maximum likelihood estimation. This method is experimental and is not currently recommended. For this ml method the sigma can be specified with the option --sigma and the step size can be specified with the --step option.
You can set a threshold (--threshold) to have the tensor estimated to only a subset of voxels. All the baseline voxel value higher than the threshold define the voxels where the tensors are computed. If not specified the threshold is calculated using an OTSU threshold on the baseline image.The masked generated by the -t option or by the otsu value can be saved with the --B0_mask_output option.
dtiestim also can extract a few scalar images out of the DWI set of images:
  the average baseline image (--B0) which is the average of all the B0s.
  the IDWI (--idwi)which is the geometric mean of the diffusion images.
You can also load a mask if you want to compute the tensors only where the voxels are non-zero (--brain_mask) or a negative mask and the tensors will be estimated where the negative mask has zero values (--bad_region_mask)

version: 1.1.0

documentation-url: http://www.google.com/

license:
  Copyright (c)  Casey Goodlett. All rights reserved.
  See http://www.ia.unc.edu/dev/Copyright.htm for details.
     This software is distributed WITHOUT ANY WARRANTY; without even
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
     PURPOSE.  See the above copyright notices for more information.


contributor: Casey Goodlett

acknowledgements: Hans Johnson(1,3,4); Kent Williams(1); (1=University of Iowa Department of Psychiatry, 3=University of Iowa Department of Biomedical Engineering, 4=University of Iowa Department of Electrical and Computer Engineering) provided conversions to make DTIProcess compatible with Slicer execution, and simplified the stand-alone build requirements by removing the dependancies on boost and a fortran compiler.

"""

    input_spec = dtiestimInputSpec
    output_spec = dtiestimOutputSpec
    _cmd = " dtiestim "
    _outputs_filenames = {'tensor_output':'tensor_output.nii','idwi':'idwi.nii','B0':'B0.nii','B0_mask_output':'B0_mask_output.nii'}


class dtiprocessInputSpec(CommandLineInputSpec):
    verbose = traits.Bool(desc="produce verbose output", argstr="--verbose ")
    mask = File(desc="Mask tensors. Specify --outmask if you want to save the masked tensor field, otherwise the mask is applied just for the current processing ", exists=True, argstr="--mask %s")
    outmask = File(desc="Name of the masked tensor field.", exists=True, argstr="--outmask %s")
    fa_output = traits.Either(traits.Bool, File(), hash_files=False, desc="FA output file", argstr="--fa_output %s")
    md_output = traits.Either(traits.Bool, File(), hash_files=False, desc="MD output file", argstr="--md_output %s")
    fa_gradient_output = traits.Either(traits.Bool, File(), hash_files=False, desc="FA Gradient output file", argstr="--fa_gradient_output %s")
    sigma = traits.Float(desc="Scale of gradients", argstr="--sigma %f")
    fa_gradmag_output = traits.Either(traits.Bool, File(), hash_files=False, desc="FA Gradient Magnitude output file", argstr="--fa_gradmag_output %s")
    color_fa_output = traits.Either(traits.Bool, File(), hash_files=False, desc="Color FA output file", argstr="--color_fa_output %s")
    principal_eigenvector_output = traits.Either(traits.Bool, File(), hash_files=False, desc="Principal Eigenvectors Output", argstr="--principal_eigenvector_output %s")
    negative_eigenvector_output = traits.Either(traits.Bool, File(), hash_files=False, desc="Negative Eigenvectors Output: create a binary image where if any of the eigen value is below zero, the voxel is set to 1, otherwise 0.", argstr="--negative_eigenvector_output %s")
    frobenius_norm_output = traits.Either(traits.Bool, File(), hash_files=False, desc="Frobenius Norm Output", argstr="--frobenius_norm_output %s")
    lambda1_output = traits.Either(traits.Bool, File(), hash_files=False, desc="Lambda 1 (largest eigenvalue) output", argstr="--lambda1_output %s")
    lambda2_output = traits.Either(traits.Bool, File(), hash_files=False, desc="Lambda 2 (middle eigenvalue) output", argstr="--lambda2_output %s")
    lambda3_output = traits.Either(traits.Bool, File(), hash_files=False, desc="Lambda 3 (smallest eigenvalue) output", argstr="--lambda3_output %s")
    RD_output = traits.Either(traits.Bool, File(), hash_files=False, desc="RD (radial diffusivity 1/2*(lambda2+lambda3)) output", argstr="--RD_output %s")
    scalar_float = traits.Bool(desc="Write scalar [FA,MD] as unscaled float (with their actual values, otherwise scaled by 10 000).  Also causes FA to be unscaled [0..1].", argstr="--scalar_float ")
    rot_output = traits.Either(traits.Bool, File(), hash_files=False, desc="Rotated tensor output file.  Must also specify the dof file.", argstr="--rot_output %s")
    dof_file = traits.Either(traits.Bool, File(), hash_files=False, desc="Transformation file for affine transformation.  This can be ITK format (or the outdated RView).", argstr="--dof_file %s")
    deformation_output = traits.Either(traits.Bool, File(), hash_files=False, desc="Warped tensor field based on a deformation field.  This option requires the --forward,-F transformation to be specified.", argstr="--deformation_output %s")
    forward = traits.Either(traits.Bool, File(), hash_files=False, desc="Forward transformation.  Assumed to be a deformation field in world coordinates, unless the --h-field option is specified.", argstr="--forward %s")
    hField = traits.Bool(desc="forward and inverse transformations are h-fields instead of displacement fields", argstr="--hField ")
    interpolation = traits.Enum("nearestneighbor", "linear", "cubic", desc="Interpolation type (nearestneighbor, linear, cubic)", argstr="--interpolation %s")
    reorientation = traits.Enum("fs", "ppd", desc="Reorientation type (fs, ppd)", argstr="--reorientation %s")
    dti_image = File(desc="DTI tensor volume", exists=True, argstr="--dti_image %s")
    newdof_file = File(desc="Transformation file for affine transformation.  RView NEW format. (txt file output of dof2mat)", exists=True, argstr="--newdof_file %s")
    affineitk_file = File(desc="Transformation file for affine transformation.  ITK format.", exists=True, argstr="--affineitk_file %s")


class dtiprocessOutputSpec(TraitedSpec):
    fa_output = File(desc="FA output file", exists=True)
    md_output = File(desc="MD output file", exists=True)
    fa_gradient_output = File(desc="FA Gradient output file", exists=True)
    fa_gradmag_output = File(desc="FA Gradient Magnitude output file", exists=True)
    color_fa_output = File(desc="Color FA output file", exists=True)
    principal_eigenvector_output = File(desc="Principal Eigenvectors Output", exists=True)
    negative_eigenvector_output = File(desc="Negative Eigenvectors Output: create a binary image where if any of the eigen value is below zero, the voxel is set to 1, otherwise 0.", exists=True)
    frobenius_norm_output = File(desc="Frobenius Norm Output", exists=True)
    lambda1_output = File(desc="Lambda 1 (largest eigenvalue) output", exists=True)
    lambda2_output = File(desc="Lambda 2 (middle eigenvalue) output", exists=True)
    lambda3_output = File(desc="Lambda 3 (smallest eigenvalue) output", exists=True)
    RD_output = File(desc="RD (radial diffusivity 1/2*(lambda2+lambda3)) output", exists=True)
    rot_output = File(desc="Rotated tensor output file.  Must also specify the dof file.", exists=True)
    dof_file = File(desc="Transformation file for affine transformation.  This can be ITK format (or the outdated RView).", exists=True)
    deformation_output = File(desc="Warped tensor field based on a deformation field.  This option requires the --forward,-F transformation to be specified.", exists=True)
    forward = File(desc="Forward transformation.  Assumed to be a deformation field in world coordinates, unless the --h-field option is specified.", exists=True)


class dtiprocess(SEMLikeCommandLine):
    """title: dtiprocess

category: Diffusion.DTIProcess

description:
dtiprocess is a tool that handles tensor fields. It takes as an input a tensor field in nrrd format.
It can generate diffusion scalar properties out of the tensor field such as : FA (--fa_output), Gradient FA image (--fa_gradient_output), color FA (--color_fa_output), MD (--md_output), Frobenius norm (--frobenius_norm_output), lbd1, lbd2, lbd3 (--lambda{1,2,3}_output), binary map of voxel where if any of the eigenvalue is negative, the voxel is set to 1 (--negative_eigenvector_output)
It also creates 4D images out of the tensor field such as: Highest eigenvector map (highest eigenvector at each voxel) (--principal_eigenvector_output)
 Masking capabilities: For any of the processing done with dtiprocess, it's possible to apply it on a masked region of the tensor field. You need to use the --mask option for any of the option to be applied on that tensor field sub-region only. If you want to save the masked tensor field use the option --outmask and specify the new masked tensor field file name.
dtiprocess also allows a range of transformations on the tensor fields. The transformed tensor field file name is specified with the option --deformation_output. There are 3 resampling interpolation methods specified with the tag --interpolation followed by the type to use (nearestneighbor, linear, cubic) Then you have several transformations possible to apply:
  - Affine transformations using as an input
  - itk affine transformation file (based on the itkAffineTransform class)
  - Affine transformations using rview (details and download at http://www.doc.ic.ac.uk/~dr/software/). There are 2 versions of rview both creating transformation files called dof files. The old version of rview outputs text files containing the transformation parameters. It can be read in with the --dof_file option. The new version outputs binary dof files. These dof files can be transformed into human readable file with the dof2mat tool which is part of the rview package. So you need to save the output of dof2mat into a text file which can then be used with the -- newdof_file option. Usage example: dof2mat mynewdoffile.dof >> mynewdoffile.txt    dtiprocess --dti_image mytensorfield.nhdr --newdof_file mynewdoffile.txt --rot_output myaffinetensorfield.nhdr
Non linear transformations as an input: The default transformation file type is d-field (displacement field) in nrrd format. The option to use is --forward with the name of the file. If the transformation file is a h-field you have to add the option --hField.

version: 1.0.0

documentation-url: http://www.google.com/

license:
  Copyright (c)  Casey Goodlett. All rights reserved.
  See http://www.ia.unc.edu/dev/Copyright.htm for details.
     This software is distributed WITHOUT ANY WARRANTY; without even
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
     PURPOSE.  See the above copyright notices for more information.


contributor: Casey Goodlett

"""

    input_spec = dtiprocessInputSpec
    output_spec = dtiprocessOutputSpec
    _cmd = " dtiprocess "
    _outputs_filenames = {'fa_gradmag_output':'fa_gradmag_output.nii','fa_gradient_output':'fa_gradient_output.nii','lambda1_output':'lambda1_output.nii','lambda2_output':'lambda2_output.nii','color_fa_output':'color_fa_output.nii','fa_output':'fa_output.nii','frobenius_norm_output':'frobenius_norm_output.nii','principal_eigenvector_output':'principal_eigenvector_output.nii','forward':'forward.nii','dof_file':'dof_file','lambda3_output':'lambda3_output.nii','negative_eigenvector_output':'negative_eigenvector_output.nii','md_output':'md_output.nii','RD_output':'RD_output.nii','deformation_output':'deformation_output.nii','rot_output':'rot_output.nii'}
import pixellib
from pixellib.semantic import semantic_segmentation


def object_detection_on_an_image(image, model):
    segment_image = semantic_segmentation()
    segment_image.load_ade20k_model("weights/" + model)

    target_class = segment_image.select_target_classes(person=True)

    result = segment_image.segmentAsAde20k(
        image_path="images/" + image,
        show_bboxes=True,
        # segment_target_classes=target_class,
        # extract_segmented_objects=True,
        # save_extracted_objects=True,
        output_image_name=image
    )

    print(result[0]["scores"])
    objects_count = len(result[0]["scores"])
    if objects_count > 1:
        print(f"Объектов: {objects_count}")
        found = True
        print(found)
    else:
        print(f"Объектов: {objects_count}")
        found = False
        print(found)       
    


    # print(f"Объектов: {objects_count}")


def main():
    object_detection_on_an_image("1.jpg", "deeplabv3_xception65_ade20k.h5")


if __name__ == '__main__':
    main()
